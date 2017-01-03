import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

class WhoAmI:
	"""Who am i"""
	def hostname(self):
		return socket.gethostname()

	def IP(self):
		return socket.gethostbyname(self.hostname())

	def fqdn(self):
		return socket.getfqdn()

def run():
	x = WhoAmI()
	print("Hostname:", x.hostname())
	print("IP:", x.IP())
	print("FQDN:", x.fqdn())

run()
