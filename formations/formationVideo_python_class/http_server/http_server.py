#coding:utf-8

""" HTTP server
-------------------""" 

import http.server
import socketserver

port = 80
address = ("", port)

# standard HTTP request manager
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print(f"server started on port {port}")

httpd.serve_forever()