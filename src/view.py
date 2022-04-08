import tkinter
from .entryScreen import EntryScreen
from .playScreen import PlayScreen
from tkinter import Tk, Button
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./gui_assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class View:

	# Default constructor
	def __init__(self):
		# create main window
		self.root = Tk()
		# get screen dimensions
		self.SCREEN_HEIGHT = self.root.winfo_screenheight()
		self.SCREEN_WIDTH = self.root.winfo_screenwidth()
		# set window dimensions
		self.WINDOW_WIDTH = 960
		self.WINDOW_HEIGHT = 768
		# calculate center of screen
		self.CENTER_HEIGHT = (self.SCREEN_HEIGHT//2) - (self.WINDOW_HEIGHT//2)
		self.CENTER_WIDTH = (self.SCREEN_WIDTH//2) - (self.WINDOW_WIDTH//2)
		# set opening position of window to center
		self.root.geometry(f'{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{self.CENTER_WIDTH}+{self.CENTER_HEIGHT}')
		self.root.configure(bg = "black")
		self.root.title('Player Entry Screen')
		self.root.resizable(False, False)
		# create frame that screens transition on
		self.main_frame = tkinter.Frame(self.root,height=self.WINDOW_HEIGHT,width=self.WINDOW_WIDTH,bg='white')
		self.main_frame.pack()
		# initialize screen variables
		self.entry_screen = None
		self.play_screen = None
		self.current_screen = ""
		# initialize controller
		self.controller = None
		# create buttons
		self.create_buttons()
		# create entry screen frame
		self.create_entry_screen()

	# Set controller
	def setController(self, controller):
		self.controller = controller

	# Creates entry screen and buttons
	def create_entry_screen(self):
		self.entry_screen = EntryScreen(self.main_frame, self)
		self.entry_screen.window.pack(fill= "both", expand=True)
		self.entry_screen.window.tkraise()
		self.current_screen = "entry"

	# swaps to play screen
	def to_play_screen(self):
		if self.current_screen == "play":
			print('already on play screen!')
			return
		self.play_screen = PlayScreen(self.main_frame, self.entry_screen, self)
		self.entry_screen.window.forget()
		self.play_screen.window.pack(fill= "both", expand=True)
		self.play_screen.update_score()
		self.current_screen = "play"

	# swap back to entry screen
	def to_entry_screen(self):
		if self.current_screen == "entry":
			print('already on entry screen!')
			return
		# destroy socket thread
		self.play_screen.game_Socket.stop()
		self.play_screen.window.destroy()
		self.entry_screen.window.pack(fill= "both", expand=True)
		self.entry_screen.window.tkraise()
		self.current_screen = "entry"

	# create buttons
	def create_buttons(self):
	# Code below creates the buttons at the bottom of the window
		self.button_1 = Button(
			command = lambda:self.to_entry_screen(),
			anchor="center",
			text= "F1\n Edit\n Game",
			font= ("SegoeUI", -int(self.WINDOW_WIDTH * 0.01947)),
			bg="#4B0909",
			fg="white",
			justify="center",
			highlightthickness=4,
			highlightcolor= "white",
			borderwidth=5
		)
		self.button_1.place(
			x = self.WINDOW_WIDTH / 2,
			y = self.WINDOW_HEIGHT,
			width= self.WINDOW_WIDTH * 0.109,
			height= self.WINDOW_HEIGHT * 0.109,
			anchor="se"
		)

		self.button_4 = Button(
			# image = self.button_image_4,
			command = lambda:self.to_play_screen(),
			anchor="center",
			text= "F5\n Start\n Game",
			font= ("SegoeUI", -int(self.WINDOW_WIDTH * 0.01947)),
			bg="#4B0909",
			fg="white",
			justify="center",
			highlightthickness=4,
			highlightcolor= "white",
			borderwidth=5
		)
		self.button_4.place(
			x = self.WINDOW_WIDTH / 2,
			y = self.WINDOW_HEIGHT,
			width= self.WINDOW_WIDTH * 0.109,
			height= self.WINDOW_HEIGHT * 0.109,
			anchor="sw"
		)
		# bind F-keys to their corresponding button
		self.root.bind_all('<F5>', lambda event: self.button_4.invoke())
		self.root.bind_all('<F1>', lambda event: self.button_1.invoke())