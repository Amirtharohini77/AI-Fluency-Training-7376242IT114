import re
from config import CANTEEN_PRICES, QUESTIONS


def workflow(question):
    items = re.findall(r"[A-Z]+", question.upper())
    prices = [CANTEEN_PRICES[item] for item in items if item in CANTEEN_PRICES]

    if not prices:
        return "Sorry, I can only answer questions about canteen prices."

    text = question.lower()

    if "total" in text:
        total = sum(prices)

        percent = re.search(r"(\d+)\s*%", text)

        if "discount" in text and percent:
            total = total * (1 - int(percent.group(1)) / 100)

        return f"Total price: Rs. {total:,.0f}"

    if "more expensive" in text and len(prices) == 2:
        difference = prices[0] - prices[1]

        if difference > 0:
            return f"Yes, difference: Rs. {difference:,}"
        elif difference < 0:
            return f"No, difference: Rs. {abs(difference):,}"
        else:
            return "They have the same price."

    if len(prices) == 1:
        return f"Price: Rs. {prices[0]:,}"

    return "Sorry, I do not have a rule for this type of question."


if __name__ == "__main__":
    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW (no LLM) ===\n")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)