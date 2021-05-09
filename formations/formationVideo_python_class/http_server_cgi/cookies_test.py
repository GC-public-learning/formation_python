#!/usr/bin/python3

import http.cookies
import datetime
import os
import cgi
import sys
import codecs

# force utf-8 with the print function (handle accents)
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

"""
cookies sub attributes
--------------------
expires
path
comment
domain
max-age (not compatible everywhere)
secure
version 
httponly
"""

# create cookie
my_cookie = http.cookies.SimpleCookie()

# setup cookies
my_cookie["pref_lang"] = "en-US"

expiration = datetime.datetime.now() + datetime.timedelta(days=365)
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%S")
my_cookie["pref_lang"]["expires"] = expiration

# sub index are case insensitive ! ->
my_cookie["pref_lang"]["httpONly"] = True

# use cookie
my_cookie.output()


# handling cookie

# handle cookie with environement variable

try:
	user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
except(http.cookies.CookieError, KeyError):
	pass



header = """<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>form</title>
</head>
<body>"""

footer = """</body></html>"""

content = f"""<h1>cookies</h1>
<p>{my_cookie}</p>
<p>prefered language : {user_lang["pref_lang"].value}</p>"""

# display
print("Content-Type:text/html; charset=utf-8\n")
print(header)
print(content)
print(footer)
