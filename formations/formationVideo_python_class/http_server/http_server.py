#coding:utf-8

""" HTTP server
-------------------""" 
# need to be root to be executed

import http.server
import socketserver

port = 80
address = ("", port)

# standard HTTP request manager
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print(f"server started on port {port}")

httpd.serve_forever()