"""Day 5: call the Ollama REST API directly."""

import json
import time

import requests


BASE = "http://localhost:11434"
MODEL = "qwen2.5:1.5b"
PROMPT = "In three sentences, explain what an AI agent is."


def list_models():

    tags = requests.get(
        f"{BASE}/api/tags",
        timeout=30
    ).json()

    print("Models on disk:")

    for model in tags.get("models", []):

        size_gb = model.get("size", 0) / 1e9

        print(
            f"   {model['name']:<28} "
            f"{size_gb:5.2f} GB"
        )


def loaded_models():

    running = requests.get(
        f"{BASE}/api/ps",
        timeout=30
    ).json().get("models", [])

    if not running:

        print("Nothing is loaded in memory.")

    for model in running:

        print(
            f"   loaded: {model['name']} "
            f"{model.get('size', 0) / 1e9:5.2f} GB"
        )


def generate_once(
    model=MODEL,
    prompt=PROMPT
):

    start = time.time()

    response = requests.post(
        f"{BASE}/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    ).json()

    elapsed = time.time() - start

    tokens = response.get(
        "eval_count",
        0
    )

    print(
        f"\n[generate] "
        f"{elapsed:.1f} s for "
        f"{tokens} tokens "
        f"({tokens / elapsed if elapsed else 0:.1f} tokens/s)"
    )

    print(
        response.get(
            "response",
            ""
        ).strip()[:300]
    )


def chat_streaming(
    model=MODEL,
    prompt=PROMPT
):

    start = time.time()

    first_token_at = None
    pieces = []


    with requests.post(
        f"{BASE}/api/chat",
        json={
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": True
        },
        stream=True,
        timeout=300
    ) as response:

        for line in response.iter_lines():

            if not line:
                continue

            chunk = json.loads(line)

            piece = chunk.get(
                "message",
                {}
            ).get(
                "content",
                ""
            )

            if (
                piece
                and first_token_at is None
            ):

                first_token_at = (
                    time.time() - start
                )

            pieces.append(piece)


    total = time.time() - start

    text = "".join(pieces)


    print(
        f"\n[chat, streaming] "
        f"TTFT "
        f"{first_token_at:.2f} s | "
        f"total {total:.1f} s | "
        f"{len(text)} characters"
    )

    print(
        text.strip()[:300]
    )


def openai_compatible(
    model=MODEL,
    prompt=PROMPT
):

    response = requests.post(
        f"{BASE}/v1/chat/completions",
        headers={
            "Authorization": "Bearer ollama"
        },
        json={
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0
        },
        timeout=300
    ).json()

    print("\n[/v1/chat/completions]")

    print(
        response["choices"][0]
        ["message"]["content"]
        .strip()[:300]
    )


if __name__ == "__main__":

    list_models()
    generate_once()
    chat_streaming()
    openai_compatible()

    print()

    loaded_models()