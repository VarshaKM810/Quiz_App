import sys
import os

# Add the current directory to path
sys.path.append(os.getcwd())

from database import SessionLocal, engine
import models
import auth
from sqlalchemy.orm import Session
import traceback

def test_signup():
    db = SessionLocal()
    try:
        username = "testuser"
        email = "test@example.com"
        password = "password123"
        
        # Check if exists
        db_user = db.query(models.User).filter(models.User.username == username).first()
        if db_user:
            print(f"User {username} already exists, deleting to re-test...")
            db.delete(db_user)
            db.commit()
            
        print(f"Attempting signup for {username}...")
        hashed_password = auth.get_password_hash(password)
        print(f"Hashed password: {hashed_password[:10]}...")
        
        new_user = models.User(username=username, email=email, hashed_password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print(f"Successfully signed up user: {new_user.username} (ID: {new_user.id})")
        
    except Exception as e:
        print("ERROR DURING SIGNUP:")
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test_signup()
