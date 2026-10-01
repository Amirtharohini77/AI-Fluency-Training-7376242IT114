import json

from assessment_config import client, MODEL
from assessment_tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = (
    "You are a college library assistant. "
    "Never guess library availability. "
    "Always use get_book_copies when a book availability "
    "question is asked. "
    "Use calculator for arithmetic. "
    "Available book codes are AI202, PY101 and DB201. "
    "Use tools when necessary and answer directly when tools "
    "are not required."
)


def agent(question, max_steps=8):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            parallel_tool_calls=False,
            temperature=0
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return (message.content or "").strip()

        messages.append({
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": call.function.name,
                        "arguments": call.function.arguments
                    }
                }
                for call in message.tool_calls
            ]
        })

        for call in message.tool_calls:

            name = call.function.name

            arguments = json.loads(
                call.function.arguments or "{}"
            )

            function = TOOL_FUNCTIONS.get(name)

            result = (
                function(**arguments)
                if function
                else f"Unknown tool: {name}"
            )

            print(
                f"step {step}: "
                f"{name}({arguments}) -> {result}"
            )

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

    return "Stopped: maximum steps reached."


if __name__ == "__main__":

    questions = [
        (
            "Five students want to borrow AI202. "
            "How many copies are available and how many "
            "students cannot borrow it right now?"
        ),
        (
            "A student has 3 study sessions of 50 minutes each, "
            "with a 10-minute break between each session. "
            "How much total time does the schedule take?"
        ),
        (
            "A lab has 18 computers. Each computer is shared "
            "by 2 students in the morning and 3 students in "
            "the afternoon. How many student sittings happen "
            "in one day?"
        ),
        (
            "Ravi read more pages than Kumar. Kumar read more "
            "pages than Arun. Priya read fewer pages than Arun. "
            "Who read the most and who read the least?"
        )
    ]

    print("=== REACT AGENT ===")

    for question in questions:

        print("\nQ:", question)

        answer = agent(question)

        print("A:", answer)
        print("-" * 70)