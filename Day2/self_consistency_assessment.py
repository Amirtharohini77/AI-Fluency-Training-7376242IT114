from collections import Counter

from assessment_config import client, MODEL


QUESTION = (
    "A student has 3 study sessions of 50 minutes each, "
    "with a 10-minute break between each session. "
    "How much total time does the schedule take?"
)


COT_PROMPT = (
    "You are a helpful assistant. Solve the problem step by step. "
    "Show the important calculations briefly. "
    "Finish with: Final Answer: <answer>"
)


def get_answer(text):

    for line in reversed(text.splitlines()):

        if "final answer" in line.lower():
            return line.split(":", 1)[-1].strip()

    return text.splitlines()[-1].strip()


def run_many(question, runs=5, temperature=0.8):

    answers = []

    for number in range(1, runs + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": COT_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=temperature
        )

        answer = get_answer(
            response.choices[0].message.content
        )

        print(f"run {number}: {answer}")

        answers.append(answer)

    return answers


if __name__ == "__main__":

    print("=== SELF-CONSISTENCY ===")
    print("QUESTION:", QUESTION)
    print()

    answers = run_many(
        QUESTION,
        runs=5,
        temperature=0
    )

    winner, count = Counter(
        answers
    ).most_common(1)[0]

    print(
        f"\nMajority answer "
        f"({count} of {len(answers)}): {winner}"
    )