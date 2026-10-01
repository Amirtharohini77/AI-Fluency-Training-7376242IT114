"""Tools for the canteen-price AI agent."""

import ast
import operator
from config import CANTEEN_PRICES


def get_item_price(item_name: str) -> str:
    """Look up the price for one canteen item."""
    price = CANTEEN_PRICES.get(item_name.strip().upper())

    return (
        str(price)
        if price is not None
        else f"Unknown item: {item_name}"
    )


_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def _evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.left),
            _evaluate(node.right),
        )

    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.operand)
        )

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression."""
    try:
        return str(
            _evaluate(
                ast.parse(expression, mode="eval").body
            )
        )
    except Exception as error:
        return f"Calculator error: {error}"


TOOL_FUNCTIONS = {
    "get_item_price": get_item_price,
    "calculator": calculator,
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_item_price",
            "description": (
                "Get the price in rupees for one canteen item, "
                "such as IDLI, BIRYANI, or JUICE."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {
                        "type": "string",
                        "description": (
                            "Canteen item such as IDLI, BIRYANI, or JUICE."
                        )
                    }
                },
                "required": ["item_name"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Evaluate an arithmetic expression using "
                "+ - * / and brackets."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": (
                            "Example: (40 + 120) * 0.9"
                        ),
                    }
                },
                "required": ["expression"],
                "additionalProperties": False,
            },
        },
    },
]


if __name__ == "__main__":
    print(
        "get_item_price('biryani') ->",
        get_item_price("biryani")
    )

    print(
        "calculator('(40 + 120) * 0.9') ->",
        calculator("(40 + 120) * 0.9")
    )

    print(
        "calculator('50 - 40') ->",
        calculator("50 - 40")
    )