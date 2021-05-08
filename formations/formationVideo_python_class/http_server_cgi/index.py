#!/usr/bin/python3

# ! With linux GUI, obligation to change file permissions :
# make the file executable and readable by all users -> chmod 755

# replace the traditional header "#coding:utf-8" by #!/usr/bin/python3
# because the file need to be recognized as a python script

# mendatory instruction to define the content-type
print("Content-Type:text/html; charset=utf-8\n")


header = """<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>web pagew ith python and html</title>
</head>
<body>"""

footer = """</body></html>"""

print(header)
print("<h1>Welcome to the index.py webpage !</h1>")
print(footer)