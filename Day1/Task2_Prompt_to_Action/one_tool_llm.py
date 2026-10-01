import json

from task_config import client, MODEL
from course_tool import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = (
    "You are a helpful college assistant. "
    "For questions about private course fees, "
    "use the get_course_fee tool. "
    "Never guess a private course fee. "
    "For questions that do not require private course data, "
    "answer directly."
)


QUESTIONS = [
    "What is the fee for AI202?",
    "What is 2 + 2?",
    "Write a two-line welcome message for new AI students."
]


def ask(question):

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


    # First LLM call
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
        temperature=0
    )

    message = response.choices[0].message


    # No tool needed
    if not message.tool_calls:

        return message.content.strip()


    # Record the tool request
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


    # Execute the tool
    for call in message.tool_calls:

        name = call.function.name

        arguments = json.loads(
            call.function.arguments or "{}"
        )

        print(
            "Tool call:",
            name,
            arguments
        )

        function = TOOL_FUNCTIONS.get(name)

        if function is None:

            result = (
                f"Unknown tool: {name}"
            )

        else:

            result = function(
                **arguments
            )

        print(
            "Tool result:",
            result
        )

        messages.append({
            "role": "tool",
            "tool_call_id": call.id,
            "content": str(result)
        })


    # Second LLM call:
    # model uses the tool result to answer
    final_response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )

    return (
        final_response
        .choices[0]
        .message
        .content
        .strip()
    )


if __name__ == "__main__":

    print("=== LLM WITH ONE TOOL ===")

    for question in QUESTIONS:

        print("\nQ:", question)

        answer = ask(question)

        print("A:", answer)

        print("-" * 60)