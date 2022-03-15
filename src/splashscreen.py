from tkinter import *
from PIL import Image, ImageTk

#Creates Tkinter reference
root = Tk()

class SplashScreen:

	#default constructor
	def __init__(self):

        #Opens logo image using pill
		self.logo = Image.open('src/gui_assets/Logo.png')

		#Opens background image using pill
		self.background = Image.open("src/gui_assets/background.png")

		self.image_resizing()
		self.displaySplash()


	#Method to resize the logo and background image
	def image_resizing(self):

		#Get the current screen width and height
		self.screen_width = root.winfo_screenwidth()
		self.screen_height = root.winfo_screenheight()

		#Resizes the background image to screen dimensions
		bg_resize = self.background.resize((self.screen_width, self.screen_height))

		#Sets resized image under Tkinter
		self.background = ImageTk.PhotoImage(bg_resize)

		#Grabs logo's width and height
		logo_width, logo_height = self.logo.size

		#Ratio used to either reduce or enlarge the logo
		resize_logo_ratio = 1.4

		#Changes the logo's dimensions by the resize_ratio
		logo_width = int(logo_width * resize_logo_ratio)
		logo_height = int(logo_height * resize_logo_ratio)

		#Resizes the logo to the new dimensions with pillow
		resize_logo = self.logo.resize((logo_width, logo_height))

		#Sets resized logo  under Tkinter
		self.logo = ImageTk.PhotoImage(resize_logo)



	#displays the splash screen with logo for 3 seconds and then closes
	def displaySplash(self):

		#Sets window title of screen
		root.title("Splash Screen")

		#Text displayed on splash screen
		splash_text = "Studio 12"

		#Determines the length in seconds of how long the splash screen will be on screen
		splash_duration = 5

		#Creates a canvas for text and images, highlightthickness gets rid of white border around it
		canvas = Canvas(root, highlightthickness = 0)

		#Creates the canvas background image; anchor just sets top let point (0,0) to northwest of screen
		canvas.create_image(0, 0, image = self.background, anchor = 'nw')

		#Creaets canvas text; first 2 parameters are location; fill is text color; anchor centers horizontally (like in a word document)
		canvas.create_text(self.screen_width/2, (self.screen_height/2 - (self.screen_height * 0.27)), text = splash_text, font= 'silom 80 bold', fill = 'white', anchor = 'center')

		#Creates canvas logo image; should be lower than canvas text
		canvas.create_image(self.screen_width/2, self.screen_height/2, image = self.logo, anchor = 'center')

		#Packs canvas to screen; fill & pack make the canvas and objects fill to their size rather than get cut off
		canvas.pack(fill = "both", expand = True)

		#Sets splash screen to fullscreen
		root.wm_attributes('-fullscreen', 'True')

		#after specfied time destroy splash screen
		root.after(splash_duration * 1000, root.destroy)

		#Holds splash open until duration runs out
		root.mainloop()
