import sys
import os

# Add the current directory to path
sys.path.append(os.getcwd())

from database import SessionLocal, engine
import models
from sqlalchemy import inspect

def check_db():
    try:
        # Try to connect
        connection = engine.connect()
        print("Successfully connected to the database.")
        
        # Check tables
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"Tables in database: {tables}")
        
        if 'users' in tables:
            columns = [c['name'] for c in inspector.get_columns('users')]
            print(f"Columns in 'users' table: {columns}")
            
            # Required columns for signup: username, email, hashed_password
            required = ['username', 'email', 'hashed_password']
            missing = [r for r in required if r not in columns]
            if missing:
                print(f"CRITICAL: Missing columns in 'users' table: {missing}")
            else:
                print("All required columns for 'users' are present.")
        else:
            print("CRITICAL: 'users' table not found.")
            
        connection.close()
    except Exception as e:
        print(f"Error checking database: {e}")

if __name__ == "__main__":
    check_db()
