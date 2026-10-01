from task_config import client, MODEL


QUESTIONS = [
    "What is the fee for AI202?",
    "What is 2 + 2?",
    "Write a two-line welcome message for new AI students."
]


SYSTEM_PROMPT = (
    "You are a helpful college assistant. "
    "Answer directly from your own knowledge. "
    "You do not have access to private college data "
    "or external tools."
)


def ask(question):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    print("=== PLAIN LLM - NO TOOL ===")

    for question in QUESTIONS:

        print("\nQ:", question)
        print("A:", ask(question))
        print("-" * 60)