#!/usr/bin/python3

header = """<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>form</title>
</head>
<body>"""

footer = """</body></html>"""

content = """<h1>form</h1>
<form method="post" action="result.py">
	<p>
		<input type="text" name="username">
		<input type="submit" value="send">
	<p>
</form>
"""

# display
print("Content-Type:text/html; charset=utf-8\n")
print(header)
print(content)
print(footer)
