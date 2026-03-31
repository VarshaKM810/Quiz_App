from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from data import QUIZ_DATA

def init_db():
    # Create tables if they don't exist
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    print(f"Connecting to database with URL: {engine.url}")
    print("Clearing existing quiz data...")
    # Clear existing data to avoid duplicates (optional, but cleaner for this update)
    db.query(models.Option).delete()
    db.query(models.Question).delete()
    db.query(models.Material).delete()
    db.query(models.Quiz).delete()
    db.commit()

    print("Seeding new quiz data...")
    
    from data import MATERIALS_DATA
    
    # Store created quizzes to avoid duplicate categories
    quizzes = {}

    # Initial Pass: Create Quizzes and Materials
    for m_item in MATERIALS_DATA:
        category = m_item["category"]
        quiz_title = f"{category.upper()} Quiz"
        if category == "js":
            quiz_title = "JavaScript Quiz"
        elif category == "cpp":
            quiz_title = "C++ Quiz"
        elif category == "html":
            quiz_title = "HTML Quiz"
        elif category == "css":
            quiz_title = "CSS Quiz"
        elif category == "sql":
            quiz_title = "SQL Quiz"
        
        new_quiz = models.Quiz(
            title=quiz_title,
            description=f"Test your {category.upper()} knowledge"
        )
        db.add(new_quiz)
        db.commit()
        db.refresh(new_quiz)
        quizzes[category] = new_quiz

        # Add Material for this quiz
        new_material = models.Material(
            quiz_id=new_quiz.id,
            title=m_item["title"],
            content=m_item["content"]
        )
        db.add(new_material)
        db.commit()

    # Second Pass: Add Questions and Options
    for item in QUIZ_DATA:
        category = item["category"]
        
        # In case a category didn't have material but has questions
        if category not in quizzes:
            quiz_title = f"{category.upper()} Quiz"
            new_quiz = models.Quiz(
                title=quiz_title,
                description=f"Test your {category.upper()} knowledge"
            )
            db.add(new_quiz)
            db.commit()
            db.refresh(new_quiz)
            quizzes[category] = new_quiz

        # Add Question
        quiz = quizzes[category]
        new_question = models.Question(
            quiz_id=quiz.id,
            question_text=item["text"],
            difficulty=1 # Default to easy for seeded questions
        )
        db.add(new_question)
        db.commit()
        db.refresh(new_question)

        # Add Options
        correct_id = item["correct_answer"]
        for opt in item["options"]:
            is_correct = (opt["id"] == correct_id)
            new_option = models.Option(
                question_id=new_question.id,
                option_text=opt["text"],
                is_correct=is_correct
            )
            db.add(new_option)
        
        db.commit()

    db.close()
    print("Database initialized with expanded dataset.")

if __name__ == "__main__":
    init_db()
