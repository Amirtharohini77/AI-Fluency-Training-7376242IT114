import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


# Reuse the .env from the parent Day1 folder
load_dotenv(
    Path(__file__).resolve().parents[1] / ".env"
)


PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER != "groq":
    raise SystemExit("This task is configured for Groq.")

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise SystemExit(
        "GROQ_API_KEY not found. Check Day1/.env."
    )

MODEL = os.getenv(
    "MODEL",
    "openai/gpt-oss-20b"
)

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=API_KEY
)