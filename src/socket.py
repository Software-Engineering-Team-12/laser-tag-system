from select import select
import socket
from threading import Thread
from time import sleep

class gameSocket(Thread):
		# method for setting up socket
	def __init__(self, play_screen):
		super().__init__()
		# makes thread close when program closes
		self.setDaemon(True)
		self.localIP     = "127.0.0.1"
		self.localPort   = 20001
		self.bufferSize  = 1024
		self.msgFromServer       = "Hello UDP Client"
		self.bytesToSend         = str.encode(self.msgFromServer)
		self.keep_running = True
		self.play_screen = play_screen

		# Create a datagram socket
		self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

		# Bind to address and ip
		self.UDPServerSocket.bind((self.localIP, self.localPort))

		print("UDP server up")
	# method that runs when .start() is called
	def run(self):
		while self.keep_running:
			# debug message to show server is listening and not stalled
			# print("listening")
			# prevent from getting stuck on recvfrom
			ready_list, wait_list, x_list = select([self.UDPServerSocket], [], [], 0.5)
			if self.UDPServerSocket in ready_list:
				try:
					bytesAddressPair = self.UDPServerSocket.recvfrom(self.bufferSize)
					message = bytesAddressPair[0]
					address = bytesAddressPair[1]
					clientMsg = "Message from Client:{}".format(message)
					clientIP  = "Client IP Address:{}".format(address)
				
					print(clientMsg)
					print(clientIP)
					self.play_screen.update_action_log(message.decode("utf-8"))
					# Sending a reply to client
					self.UDPServerSocket.sendto(self.bytesToSend, address)
				except socket.error as err:
					print(f'error from receiving socket {err}')
	# method to stop server when leaving game screen
	def stop(self):
		if self.UDPServerSocket:
			self.keep_running = False
			sleep(0.5)
			self.UDPServerSocket.close()
			print("UDP server stopped")
