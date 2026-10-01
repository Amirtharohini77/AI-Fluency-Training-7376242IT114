import ast
import operator

from assessment_config import LIBRARY_DATA


def get_book_copies(book_code: str) -> str:
    """Return the number of available copies of a book."""
    copies = LIBRARY_DATA.get(book_code.strip().upper())

    if copies is None:
        return f"Unknown book code: {book_code}"

    return str(copies)


OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}


def evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(
        node.value, (int, float)
    ):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        return OPS[type(node.op)](
            evaluate(node.left),
            evaluate(node.right)
        )

    if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
        return OPS[type(node.op)](
            evaluate(node.operand)
        )

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    try:
        result = evaluate(
            ast.parse(expression, mode="eval").body
        )
        return str(result)
    except Exception as error:
        return f"Calculator error: {error}"


TOOL_FUNCTIONS = {
    "get_book_copies": get_book_copies,
    "calculator": calculator
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_book_copies",
            "description": (
                "Get the number of available copies for a "
                "library book such as AI202, PY101 or DB201."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "book_code": {
                        "type": "string",
                        "description": (
                            "Book code such as AI202, PY101 or DB201."
                        )
                    }
                },
                "required": ["book_code"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Calculate arithmetic expressions using "
                "+, -, *, / and brackets."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": (
                            "Example: 5 * 50 + 2 * 10"
                        )
                    }
                },
                "required": ["expression"],
                "additionalProperties": False
            }
        }
    }
]