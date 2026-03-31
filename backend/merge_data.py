import data
import temp_expanded_data
import os

# Combine existing questions with new ones
full_quiz_data = data.QUIZ_DATA + temp_expanded_data.EXTRA_QUESTIONS

# Get materials data
materials_data = temp_expanded_data.MATERIALS_DATA

# Write to a new file with better formatting
with open('data.py', 'w', encoding='utf-8') as f:
    f.write('QUIZ_DATA = [\n')
    for q in full_quiz_data:
        f.write(f'    {repr(q)},\n')
    f.write(']\n\n')
    
    f.write('MATERIALS_DATA = [\n')
    for m in materials_data:
        f.write(f'    {repr(m)},\n')
    f.write(']\n')

print("Data merged successfully into data.py")
