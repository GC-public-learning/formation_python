#coding:utf-8

""" HTTP server
-------------------""" 

import http.server

port = 80
address = ("", port)

server = http.server.HTTPServer

# CGI (common gateway interface) HTTP request manager
# using CGI interface (no longer work with html files !)
# -> execute files instead of read 
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
httpd = server(address, handler)

print(f"server started on port {port}")

httpd.serve_forever()