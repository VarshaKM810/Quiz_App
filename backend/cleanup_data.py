import sys
import os

# Set search path to current dir
sys.path.append(os.getcwd())

try:
    from data import QUIZ_DATA, MATERIALS_DATA
    
    seen_questions = set()
    unique_quiz_data = []
    
    for item in QUIZ_DATA:
        # Create a unique key based on text and category
        key = (item['category'], item['text'])
        if key not in seen_questions:
            seen_questions.add(key)
            unique_quiz_data.append(item)
            
    # Write back to data.py
    with open('data.py', 'w', encoding='utf-8') as f:
        f.write('QUIZ_DATA = [\n')
        for item in unique_quiz_data:
            f.write(f'    {repr(item)},\n')
        f.write(']\n\n')
        
        f.write('MATERIALS_DATA = [\n')
        for item in MATERIALS_DATA:
            f.write(f'    {repr(item)},\n')
        f.write(']\n')
    
    print(f"Deduplication complete. Original: {len(QUIZ_DATA)}, Unique: {len(unique_quiz_data)}")

except Exception as e:
    print(f"Error during deduplication: {e}")
