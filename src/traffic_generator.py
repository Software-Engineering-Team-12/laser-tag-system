import socket
import random
from threading import Thread
import time
class trafficGenerator(Thread):
	def __init__(self):
		super().__init__()
		self.running = False
		# makes thread close when program closes
		self.setDaemon(True)
		self.bufferSize  = 1024
		self.serverAddressPort   = ("127.0.0.1", 20001)
		self.red = None
		self.green = None
		self.counter = 20

		# Create datagram socket
		self.UDPClientSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	# method that runs when .start() is called
	def run(self):
		self.running = True
		# counter number of events, random player and order
		i = 1
		while i < int(self.counter):
			redplayer = random.choice(list(self.red))
			greenplayer = random.choice(list(self.green))

			if random.randint(1,2) == 1:
				message = redplayer + ":" + greenplayer
			else:
				message = greenplayer + ":" + redplayer

			i+=1;
			self.UDPClientSocketTransmit.sendto(str.encode(str(message)), self.serverAddressPort)
			time.sleep(random.randint(1,3))
			
		print("program complete")
	# allow generator to access teams
	def set_teams(self, red_team, green_team):
		self.red = red_team
		self.green = green_team