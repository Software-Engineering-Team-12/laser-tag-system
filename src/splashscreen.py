from tkinter import *
from PIL import Image, ImageTk

#Creates Tkinter reference
root = Tk()

class SplashScreen:

	#default constructor
	def __init__(self):

        #Opens using pill
		self.logo = Image.open('src/gui_assets/Logo.png')

		#Opens using pill
		self.background = Image.open("src/gui_assets/background.png")

		root.title("Splash Screen")

		self.run()

	def run(self):

		self.grab_screen_dimensions()

		self.set_window_dimensions()

		self.resize_background()

		self.resize_logo()

		self.set_canvas_placement()

		self.create_canvas()

		self.display_splash()

	def grab_screen_dimensions(self):

		self.screen_width = root.winfo_screenwidth()

		self.screen_height = root.winfo_screenheight()

	def set_window_dimensions(self):

		self.window_width = 900

		self.window_height = 600

		#Holds screen center dimensions
		self.center_window_width = (self.screen_width/2) - (self.window_width/2)
		self.center_window_height = (self.screen_height/2) - (self.window_height/2)

	def resize_background(self):

		#Resizes the background image to screen dimensions
		resized_background = self.background.resize((self.screen_width, self.screen_height))

		#Set with Tkinter
		self.background = ImageTk.PhotoImage(resized_background)

	def resize_logo(self):

		#Grabs logo's width and height
		logo_width, logo_height = self.logo.size

		#Ratio used to multiply
		resize_logo_ratio = 1.4

		resized_logo_width = int(logo_width * resize_logo_ratio)
		resized_logo_height = int(logo_height * resize_logo_ratio)

		#Resizes logo with pillow
		resized_logo = self.logo.resize((resized_logo_width, resized_logo_height))

		self.logo = ImageTk.PhotoImage(resized_logo)


	def set_canvas_placement(self):

		self.canvas_text_width = self.window_width/2

		self.canvas_image_width = self.window_width/2

		self.canvas_image_height = (self.window_height/2 - (self.window_height * 0.27))

		self.canvas_text_height = self.window_height/2

	def create_canvas(self):

		splash_text = "Studio 12"

		#create canvas
		canvas = Canvas(root, highlightthickness = 0)

		canvas.create_image(0, 0, image = self.background, anchor = 'nw')

		canvas.create_text(self.canvas_text_width, self.canvas_image_height, text = splash_text, font= 'silom 80 bold', fill = 'white', anchor = 'center')

		canvas.create_image(self.canvas_image_width, self.canvas_text_height, image = self.logo, anchor = 'center')

		#Fill & pack has the canvas and objects fill to their size rather than get cut short
		canvas.pack(fill = "both", expand = True)

	def display_splash(self):

		#In seconds
		splash_screen_duration = 2

		root.geometry('%dx%d+%d+%d' % (self.window_width, self.window_height, self.center_window_width, self.center_window_height))

		#after specfied time destroy splash screen
		root.after(splash_screen_duration * 1000, root.destroy)

		#Holds splash open until duration runs out
		root.mainloop()
