from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from datetime import datetime, timedelta
import logging
import models, database, auth, ai_handler

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="W3Schools Quiz App API")

# Enable CORS for the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "message": str(exc)},
    )

# --- Authentication Endpoints ---

@app.post("/api/signup", response_model=models.UserSchema)
def signup(user: models.UserCreate, db: Session = Depends(database.get_db)):
    db_user_name = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user_name:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    db_user_email = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/api/token", response_model=models.Token)
def login_for_access_token(user: models.UserLogin, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# --- Quiz Endpoints ---

@app.get("/api/quizzes", response_model=List[models.QuizListSchema])
def get_quizzes(db: Session = Depends(database.get_db)):
    return db.query(models.Quiz).all()

@app.get("/api/quiz/{quiz_id}", response_model=models.QuizSchema)
def get_quiz(
    quiz_id: int, 
    db: Session = Depends(database.get_db),
    current_user: Optional[models.User] = Depends(auth.get_current_user)
):
    quiz = db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    
    # Adaptive Difficulty Logic
    user_avg = db.query(func.avg(models.Score.percentage)).filter(
        models.Score.user_id == current_user.id,
        models.Score.quiz_id == quiz_id
    ).scalar() or 0
    
    # Filter questions based on user level and performance
    if user_avg > 85 or current_user.level >= 5:
        # High performance: Serve Medium and Hard questions
        adaptive_questions = [q for q in quiz.questions if q.difficulty >= 2]
    elif user_avg > 60 or current_user.level >= 3:
        # Medium performance: Mix of all, but mostly 1 and 2
        adaptive_questions = [q for q in quiz.questions if q.difficulty <= 2]
    else:
        # Beginner: Serve Easy questions
        adaptive_questions = [q for q in quiz.questions if q.difficulty == 1]
        
    # Fallback to all questions if filtering returns too few (e.g. if DB not fully seeded with all difficulties)
    if len(adaptive_questions) < 3:
        adaptive_questions = quiz.questions

    return models.QuizSchema(
        id=quiz.id,
        title=quiz.title,
        description=quiz.description,
        questions=adaptive_questions,
        material=quiz.material
    )

@app.get("/api/quiz/{quiz_id}/material", response_model=models.MaterialSchema)
def get_quiz_material(quiz_id: int, db: Session = Depends(database.get_db)):
    material = db.query(models.Material).filter(models.Material.quiz_id == quiz_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material not found for this quiz")
    return material

@app.get("/api/leaderboard", response_model=List[models.LeaderboardEntry])
def get_leaderboard(db: Session = Depends(database.get_db)):
    scores = db.query(models.Score).order_by(models.Score.percentage.desc()).limit(10).all()
    leaderboard = []
    for s in scores:
        leaderboard.append(models.LeaderboardEntry(
            username=s.user.username,
            quiz_title=s.quiz.title,
            score=s.score,
            total=s.total,
            percentage=float(s.percentage)
        ))
    return leaderboard

# --- AI & User Endpoints ---

@app.get("/api/user/profile", response_model=models.UserSchema)
def get_user_profile(current_user: models.User = Depends(auth.get_current_user)):
    return current_user

@app.get("/api/user/analytics", response_model=List[models.AnalyticsData])
def get_user_analytics(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    results = db.query(
        models.Quiz.title.label("category"),
        func.avg(models.Score.percentage).label("average_score"),
        func.count(models.Score.id).label("quizzes_taken")
    ).join(models.Score).filter(models.Score.user_id == current_user.id).group_by(models.Quiz.id).all()
    
    return [models.AnalyticsData(category=r.category, average_score=float(r.average_score), quizzes_taken=r.quizzes_taken) for r in results]

@app.post("/api/quiz/generate")
async def generate_ai_quiz(
    request: models.AIQuizRequest,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    try:
        generated_data = ai_handler.generate_quiz_json(
            topic=request.topic,
            num_questions=request.num_questions,
            difficulty=request.difficulty
        )
        
        if not generated_data:
            raise HTTPException(status_code=500, detail="AI failed to generate quiz content")
            
        questions = []
        for i, item in enumerate(generated_data):
            options = [models.OptionSchema(id=idx, option_text=opt["text"], is_correct=(opt["id"] == item["correct_answer"])) 
                      for idx, opt in enumerate(item["options"])]
            
            questions.append(models.QuestionSchema(
                id=1000 + i, 
                question_text=item["text"],
                difficulty=request.difficulty,
                options=options
            ))
            
        return models.QuizSchema(
            id=999, 
            title=f"AI: {request.topic}",
            description=f"Generated quiz for your study session on {request.topic}.",
            questions=questions
        )
    except Exception as e:
        logger.error(f"Error in AI Quiz Generation: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/submit", response_model=models.ResultSchema)
def submit_quiz(
    request: models.SubmitQuizRequest, 
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    score = 0
    total = len(request.answers)
    
    for ans in request.answers:
        # Spaced Repetition Logic (SM-2) for persistent questions
        db_question = db.query(models.Question).filter(models.Question.id == ans.question_id).first()
        
        option = db.query(models.Option).filter(
            models.Option.id == ans.option_id,
            models.Option.question_id == ans.question_id
        ).first()
        
        is_correct = option and option.is_correct
        if is_correct:
            score += 1

        if db_question:
            state = db.query(models.UserQuestionState).filter(
                models.UserQuestionState.user_id == current_user.id,
                models.UserQuestionState.question_id == ans.question_id
            ).first()
            if not state:
                state = models.UserQuestionState(
                    user_id=current_user.id, 
                    question_id=ans.question_id,
                    interval=0,
                    ease_factor=2.5
                )
                db.add(state)
            
            q = 5 if is_correct else 2
            state.last_quality = q
            state.ease_factor = max(1.3, state.ease_factor + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)))
            
            if q >= 3:
                if state.interval == 0: state.interval = 1
                elif state.interval == 1: state.interval = 6
                else: state.interval = int(state.interval * state.ease_factor)
            else:
                state.interval = 1
            state.next_review = (datetime.utcnow() + timedelta(days=state.interval)).isoformat()

    percentage = (score/total)*100 if total > 0 else 0
    xp_gained = score * 10
    
    old_level = current_user.level
    current_user.xp += xp_gained
    new_level = (current_user.xp // 1000) + 1
    level_up = new_level > old_level
    if level_up:
        current_user.level = new_level

    if percentage == 100:
        existing_badge = db.query(models.Badge).filter(
            models.Badge.user_id == current_user.id,
            models.Badge.name == "Perfect Score"
        ).first()
        if not existing_badge:
            db.add(models.Badge(
                user_id=current_user.id,
                name="Perfect Score",
                icon="Star",
                description="Achieved 100% on a quiz!"
            ))
    
    if request.quiz_id != 999: # Don't log AI session results to global leaderboards for now
        db.add(models.Score(
            user_id=current_user.id,
            quiz_id=request.quiz_id,
            score=score,
            total=total,
            percentage=int(percentage),
            xp_gained=xp_gained,
            cheating_detected=request.cheating_detected
        ))
    
    db.commit()
    db.refresh(current_user)
            
    return models.ResultSchema(
        score=score,
        total=total,
        percentage=percentage,
        xp_gained=xp_gained,
        level_up=level_up
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
