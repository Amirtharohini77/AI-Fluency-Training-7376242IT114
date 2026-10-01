"""Challenge question for the three approaches."""

from workflow import workflow
from agent import agent


QUESTION = (
    "I have Rs. 150. Which two canteen items "
    "can I buy together within my budget?"
)


print("Q:", QUESTION)

print("\nWorkflow :", workflow(QUESTION))
print("\nAgent    :", agent(QUESTION))