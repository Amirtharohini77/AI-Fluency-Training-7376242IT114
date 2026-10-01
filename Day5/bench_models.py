import time

import requests


BASE = "http://localhost:11434"

MODELS = [
    "qwen2.5:1.5b",
    "mistral"
]


PROMPTS = [
    "Reply with exactly: OK",
    "In two sentences, what is an AI agent?",
    "A course costs Rs. 18,000 with a 15% scholarship. What is payable? Show the steps."
]


def run(model, prompt):

    start = time.time()

    data = requests.post(
        f"{BASE}/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        },
        timeout=600
    ).json()

    elapsed = time.time() - start

    tokens = data.get(
        "eval_count",
        0
    )

    load_ms = (
        data.get(
            "load_duration",
            0
        ) / 1e6
    )

    return (
        elapsed,
        tokens,
        tokens / elapsed if elapsed else 0,
        load_ms,
        data.get(
            "response",
            ""
        ).strip()
    )


if __name__ == "__main__":

    for model in MODELS:

        print("=" * 72)

        print(
            "MODEL:",
            model
        )

        for prompt in PROMPTS:

            (
                elapsed,
                tokens,
                rate,
                load_ms,
                text
            ) = run(
                model,
                prompt
            )

            print(
                f"\n prompt: {prompt[:50]}"
            )

            print(
                f" {elapsed:5.1f} s | "
                f"{tokens:4d} tokens | "
                f"{rate:5.1f} tok/s | "
                f"load {load_ms:7.1f} ms"
            )

            print(
                f" answer: {text[:160]}"
            )

            print()