import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv(Path(__file__).with_name(".env"))

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

elif PROVIDER == "ollama":
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"
    MODEL = os.getenv("MODEL", "qwen2.5:1.5b")

else:
    raise SystemExit(f"Unsupported provider: {PROVIDER}")

if not API_KEY:
    raise SystemExit("No API key found. Check your Day2/.env file.")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)


LIBRARY_DATA = {
    "AI202": 2,
    "PY101": 5,
    "DB201": 3
}