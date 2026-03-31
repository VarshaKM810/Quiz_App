import sqlite3

def check_db():
    conn = sqlite3.connect('backend/quiz_app.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM quizzes")
    quiz_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM materials")
    material_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    question_count = cursor.fetchone()[0]
    
    print(f"Quizzes: {quiz_count}")
    print(f"Materials: {material_count}")
    print(f"Questions: {question_count}")
    
    cursor.execute("SELECT title FROM quizzes")
    titles = cursor.fetchall()
    print("\nQuiz Titles:")
    for t in titles:
        print(f"- {t[0]}")
    
    conn.close()

if __name__ == "__main__":
    check_db()
