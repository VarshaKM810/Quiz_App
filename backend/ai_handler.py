import os
import json
import logging
from typing import List, Optional
from pathlib import Path

# Read .env file directly - works in all execution contexts
_env_file = Path(__file__).resolve().parent / '.env'
if _env_file.exists():
    with open(_env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip())

logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

try:
    from google import genai
    if GEMINI_API_KEY:
        client = genai.Client(api_key=GEMINI_API_KEY)
        logger.info("Gemini client loaded successfully.")
    else:
        client = None
        logger.warning("No GEMINI_API_KEY found in environment.")
except ImportError:
    genai = None
    client = None


MOCK_QUESTIONS = {
    "default": [
        {
            "text": "Which of the following best describes a compiler?",
            "options": [
                {"id": "a", "text": "A program that translates source code to machine code"},
                {"id": "b", "text": "A program that runs code line by line without translation"},
                {"id": "c", "text": "A tool for managing database connections"},
                {"id": "d", "text": "A type of operating system kernel"}
            ],
            "correct_answer": "a"
        },
        {
            "text": "What does an API stand for?",
            "options": [
                {"id": "a", "text": "Application Processing Interface"},
                {"id": "b", "text": "Application Programming Interface"},
                {"id": "c", "text": "Advanced Protocol Integration"},
                {"id": "d", "text": "Automated Program Interaction"}
            ],
            "correct_answer": "b"
        },
        {
            "text": "Which data structure uses LIFO (Last In, First Out)?",
            "options": [
                {"id": "a", "text": "Queue"},
                {"id": "b", "text": "Linked List"},
                {"id": "c", "text": "Stack"},
                {"id": "d", "text": "Hash Map"}
            ],
            "correct_answer": "c"
        },
        {
            "text": "What is the time complexity of Binary Search?",
            "options": [
                {"id": "a", "text": "O(n)"},
                {"id": "b", "text": "O(n²)"},
                {"id": "c", "text": "O(log n)"},
                {"id": "d", "text": "O(1)"}
            ],
            "correct_answer": "c"
        },
        {
            "text": "Which HTTP method is used to update an existing resource?",
            "options": [
                {"id": "a", "text": "GET"},
                {"id": "b", "text": "POST"},
                {"id": "c", "text": "DELETE"},
                {"id": "d", "text": "PUT"}
            ],
            "correct_answer": "d"
        }
    ]
}


def generate_quiz_json(topic: str, num_questions: int = 5, difficulty: int = 1) -> Optional[List[dict]]:
    """
    Generates quiz questions using Gemini AI, or returns topic-relevant mock data.
    Difficulty: 1 (Beginner), 2 (Intermediate), 3 (Advanced)
    """
    diff_label = {1: "Beginner", 2: "Intermediate", 3: "Advanced"}.get(difficulty, "Beginner")

    if client:
        prompt = f"""You are a quiz generator. Create exactly {num_questions} multiple-choice questions about: "{topic}".
Difficulty level: {diff_label}.

Rules:
- Each question must have exactly 4 answer options (a, b, c, d)
- All options must be REALISTIC and TOPIC-SPECIFIC (no generic answers like "Option A")
- Distractors should be plausible but clearly wrong
- Return ONLY a valid JSON array, no markdown, no explanations

Required JSON format:
[
  {{
    "text": "Question here?",
    "options": [
      {{"id": "a", "text": "First realistic option"}},
      {{"id": "b", "text": "Second realistic option"}},
      {{"id": "c", "text": "Third realistic option"}},
      {{"id": "d", "text": "Fourth realistic option"}}
    ],
    "correct_answer": "b"
  }}
]"""

        try:
            response = client.models.generate_content(
                model='gemini-pro',
                contents=prompt
            )
            content = response.text.strip()
            # Strip markdown code fences if present
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
            return json.loads(content.strip())
        except Exception as e:
            logger.error(f"Gemini generation failed: {type(e).__name__}: {e}")
            # Fall through to mock

    # Mock mode: return pre-built topic-aware questions
    logger.warning(f"No Gemini API key set — using mock questions for topic: '{topic}'")
    questions = MOCK_QUESTIONS.get("default", [])
    # Patch the mock to reference the actual topic
    patched = []
    for i, q in enumerate(questions[:num_questions]):
        patched.append({**q, "text": q["text"].replace("a compiler", topic) if i == 0 else q["text"]})
    return patched
