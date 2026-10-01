import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER == "ollama":
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"
    MODEL = os.getenv("MODEL", "qwen2.5:1.5b")

elif PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

elif PROVIDER == "huggingface":
    BASE_URL = "https://router.huggingface.co/v1"
    API_KEY = os.getenv("HF_TOKEN")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'. "
        "Use ollama, groq or huggingface."
    )

if not API_KEY:
    raise SystemExit(
        f"No API key found for PROVIDER={PROVIDER}. "
        "Check your .env file."
    )

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

CANTEEN_PRICES = {
    "IDLI": 40,
    "BIRYANI": 120,
    "JUICE": 50
}

QUESTIONS = [
    "What is the price of BIRYANI?",
    "What is the total price of IDLI and BIRYANI after a 10% student discount?",
    "Is JUICE more expensive than IDLI, and by how much?",
    "Write a two-line message encouraging students to eat responsibly in the college canteen.",
]


def banner(system_name):
    print(
        f"\n=== {system_name} | "
        f"provider: {PROVIDER} | model: {MODEL} ===\n"
    )