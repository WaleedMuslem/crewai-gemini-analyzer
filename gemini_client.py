import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()


def setup_gemini():
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    return LLM(
        model="gemini/gemini-2.0-flash-001",
        api_key=api_key,
    )


gemini = setup_gemini()
