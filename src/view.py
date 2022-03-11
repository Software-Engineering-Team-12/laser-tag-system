import tkinter
from .entryScreen import EntryScreen
from .playScreen import PlayScreen
from tkinter import Tk
class View:

	# Default constructor
	def __init__(self):
		# create main window
		self.root = Tk()
		self.root.geometry("1027x832")
		self.root.configure(bg = "#000000")
		self.root.title('Player Entry Screen')
		self.root.resizable(False, False)
		self.root.bind('<Return>', lambda event:self.to_play_screen)
		self.main_frame = tkinter.Frame(self.root,height=747,width=1027,bg='white')
		self.main_frame.pack()
		self.entry_screen = None
		self.play_screen = None
		self.current_screen = ""
		# initialize controller
		self.controller = None
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
		self.play_screen = PlayScreen(self.main_frame, self)
		self.entry_screen.window.forget()
		self.play_screen.window.pack(fill= "both", expand=True)
		self.play_screen.window.tkraise()
		self.play_screen.update_score()
		self.current_screen = "play"

	# swap back to entry screen
	def to_entry_screen(self):
		if self.current_screen == "entry":
			print('already on entry screen!')
			return
		self.entry_screen = EntryScreen(self.main_frame, self)
		self.play_screen.window.forget()
		self.entry_screen.window.pack(fill= "both", expand=True)
		self.entry_screen.window.tkraise()
		self.current_screen = "entry"