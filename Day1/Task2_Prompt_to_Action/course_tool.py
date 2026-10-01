"""
One private-data tool for the Day 1 assessment.
"""

COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}


def get_course_fee(course_code: str) -> str:
    """
    Look up the fee for one private college course.
    """

    code = course_code.strip().upper()

    fee = COURSE_FEES.get(code)

    if fee is None:
        return f"Unknown course code: {code}"

    return str(fee)


TOOL_FUNCTIONS = {
    "get_course_fee": get_course_fee
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": (
                "Get the private college fee in rupees "
                "for a course such as CS101, AI202, or DS303."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": (
                            "Course code such as CS101, AI202, or DS303."
                        )
                    }
                },
                "required": ["course_code"],
                "additionalProperties": False
            }
        }
    }
]


if __name__ == "__main__":

    print(
        "get_course_fee('AI202') ->",
        get_course_fee("AI202")
    )

    print(
        "get_course_fee('CS101') ->",
        get_course_fee("CS101")
    )

    print(
        "get_course_fee('XXX') ->",
        get_course_fee("XXX")
    )