from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel, EmailStr
from typing import List, Optional

# --- SQLAlchemy Models ---

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    badges = relationship("Badge", back_populates="user")

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    questions = relationship("Question", back_populates="quiz")
    material = relationship("Material", back_populates="quiz", uselist=False)

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"), unique=True)
    title = Column(String)
    content = Column(String)  # Markdown/Text content
    quiz = relationship("Quiz", back_populates="material")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    question_text = Column(String)
    difficulty = Column(Integer, default=1) # 1: Easy, 2: Medium, 3: Hard
    quiz = relationship("Quiz", back_populates="questions")
    options = relationship("Option", back_populates="question")

class Option(Base):
    __tablename__ = "options"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    option_text = Column(String)
    is_correct = Column(Boolean, default=False)
    question = relationship("Question", back_populates="options")

class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    score = Column(Integer)
    total = Column(Integer)
    percentage = Column(Integer)
    xp_gained = Column(Integer, default=0)
    cheating_detected = Column(Boolean, default=False)
    user = relationship("User")
    quiz = relationship("Quiz")

class Badge(Base):
    __tablename__ = "badges"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    icon = Column(String) # lucide icon name
    description = Column(String)
    user = relationship("User", back_populates="badges")

class UserQuestionState(Base):
    __tablename__ = "user_question_states"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    interval = Column(Integer, default=0) # days
    ease_factor = Column(Float, default=2.5) # SM-2 ease factor
    next_review = Column(String) # ISO date string
    last_quality = Column(Integer) # Last user performance (0-5)

# --- Pydantic Schemas ---

class AIQuizRequest(BaseModel):
    topic: str
    num_questions: int = 5
    difficulty: int = 1

class OptionBase(BaseModel):
    option_text: str
    is_correct: bool

class OptionSchema(OptionBase):
    id: int
    class Config:
        from_attributes = True

class QuestionBase(BaseModel):
    question_text: str
    difficulty: int

class QuestionSchema(QuestionBase):
    id: int
    options: List[OptionSchema]
    class Config:
        from_attributes = True

class MaterialBase(BaseModel):
    title: str
    content: str

class MaterialSchema(MaterialBase):
    id: int
    quiz_id: int
    class Config:
        from_attributes = True

class QuizBase(BaseModel):
    title: str
    description: Optional[str] = None

class QuizSchema(QuizBase):
    id: int
    questions: List[QuestionSchema]
    material: Optional[MaterialSchema] = None
    class Config:
        from_attributes = True

class QuizListSchema(QuizBase):
    id: int
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class BadgeSchema(BaseModel):
    name: str
    icon: str
    description: str
    class Config:
        from_attributes = True

class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    xp: int
    level: int
    badges: List[BadgeSchema] = []
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class AnswerSchema(BaseModel):
    question_id: int
    option_id: int

class SubmitQuizRequest(BaseModel):
    quiz_id: int
    answers: List[AnswerSchema]
    cheating_detected: bool = False

class ResultSchema(BaseModel):
    score: int
    total: int
    percentage: float
    xp_gained: int
    level_up: bool = False

class LeaderboardEntry(BaseModel):
    username: str
    quiz_title: str
    score: int
    total: int
    percentage: float

    class Config:
        from_attributes = True

class AnalyticsData(BaseModel):
    category: str
    average_score: float
    quizzes_taken: int
