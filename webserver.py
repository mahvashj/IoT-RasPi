# IoT-RasPi
# Simple web server on RasPi

import socket
import sys

ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ms.bind(("192.168.1.24", 80))
	
except socket.error:
    print("Failed to Bind")
	sys.exit()
ms.listen(5)
while True:
	conn, addr=ms.accept()
	print("Got a request")
conn.close()
ms.close()
