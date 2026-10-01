"""Create big.html for the context-overflow experiment."""

rows = "\n".join(
    f"<tr>"
    f"<td>Student {n:04d}</td>"
    f"<td>Roll BA{n:04d}</td>"
    f"<td>Attendance {60 + n % 40}%</td>"
    f"<td>Remarks: regular attendance recorded</td>"
    f"</tr>"
    for n in range(1, 3001)
)


html = (
    "<html><body>"
    "<h1>Attendance Register</h1>"
    f"<table>{rows}</table>"
    "</body></html>"
)


open(
    "big.html",
    "w",
    encoding="utf-8"
).write(html)


print(
    f"big.html created: "
    f"{len(html):,} characters"
)