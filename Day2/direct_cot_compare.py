from assessment_config import client, MODEL


QUESTIONS = [
    (
        "A student has 3 study sessions of 50 minutes each, "
        "with a 10-minute break between each session. "
        "How much total time does the schedule take?"
    ),
    (
        "A lab has 18 computers. Each computer is shared by "
        "2 students in the morning and 3 students in the "
        "afternoon. How many student sittings happen in one day?"
    ),
    (
        "Ravi read more pages than Kumar. Kumar read more "
        "pages than Arun. Priya read fewer pages than Arun. "
        "Who read the most and who read the least?"
    )
]


DIRECT_PROMPT = (
    "You are a helpful assistant. "
    "Give only the final answer. Do not explain."
)


COT_PROMPT = (
    "You are a helpful assistant. Solve the problem step by step. "
    "Show the important calculations or reasoning briefly. "
    "Finish with: Final Answer: <answer>"
)


def ask(system_prompt, question):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
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

    print("=== DIRECT VS CHAIN-OF-THOUGHT ===")

    for number, question in enumerate(QUESTIONS, start=1):

        print("\n" + "=" * 70)
        print(f"QUESTION {number}")
        print(question)

        print("\n--- DIRECT PROMPTING ---")
        print(ask(DIRECT_PROMPT, question))

        print("\n--- CHAIN-OF-THOUGHT ---")
        print(ask(COT_PROMPT, question))