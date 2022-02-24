from tkinter import *
from PIL import Image, ImageTk
import time

class SplashScreen:

	#default constructor
	def __init__(self):
		self.logo = Image.open('src/logo.jpg')
		self.logo = self.logo.resize((700, 400), Image.ANTIALIAS)
		self.displaySplash()


	#displays the splash screen with logo for 3 seconds and then closes
	def displaySplash(self):
		root = Tk()
		root.geometry("1280x720")
		root.title('Starting...')
		root.configure(bg = "#000000")
		img = ImageTk.PhotoImage(self.logo)
		imLabel = Label(anchor = CENTER, image=img)
		imLabel.place(x = 290, y = 160)
		imLabel = Label(anchor = CENTER, text = "LOADING...")
		imLabel.place(x = 600, y = 580)
		root.after(3000, root.destroy)
		root.mainloop()