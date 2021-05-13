#!/usr/bin/python3

import cgi
import cgitb

# active debug mode
cgitb.enable()

# collect data from form
form = cgi.FieldStorage()

# checking data
# obligation to make our own exception because getvalue() on unknown or empty 
# value doesn't raise an exception (just get the value "none")
try:
	if form.getvalue("username"):
		username = form.getvalue("username")
		content = f"""<p>Hello {username} !</p>"""
	else:
		raise Exception()
except:
	content = "<p>Error ! missing username</p>"


header = """<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>form</title>
</head>
<body>"""
footer = """</body></html>"""


# display
print("Content-Type:text/html; charset=utf-8\n")
print(header)
print(content)

# java script intergration is enabled ! so dont't forget to secure your code
# against javascript injections !
print("<script>alert(\"JavaScript works !\")</script>")
print(footer)

