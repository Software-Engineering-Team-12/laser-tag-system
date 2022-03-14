import tkinter
from .entryScreen import EntryScreen
from .playScreen import PlayScreen
from tkinter import Tk, Button, PhotoImage
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
		self.root.geometry("1027x832")
		self.root.configure(bg = "#000000")
		self.root.title('Player Entry Screen')
		self.root.resizable(False, False)
		self.main_frame = tkinter.Frame(self.root,height=747,width=1027,bg='white')
		self.main_frame.pack()
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
		self.play_screen = PlayScreen(self.main_frame, self.entry_screen)
		self.entry_screen.window.forget()
		self.play_screen.window.pack(fill= "both", expand=True)
		self.play_screen.update_score()
		self.current_screen = "play"

	# swap back to entry screen
	def to_entry_screen(self):
		if self.current_screen == "entry":
			print('already on entry screen!')
			return
		self.play_screen.window.destroy()
		self.entry_screen.window.pack(fill= "both", expand=True)
		self.entry_screen.window.tkraise()
		self.current_screen = "entry"

	# create buttons
	def create_buttons(self):
				# Code below creates all of the buttons at the bottom of the window (8 buttons in total)
		self.button_image_1 = PhotoImage(
			file = relative_to_assets("button_1.png"))
		self.button_1 = Button(
			image = self.button_image_1,
			command = lambda:self.to_entry_screen(),
			relief = "flat"
		)
		self.button_1.place(
			x = 0.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)

		self.button_image_2 = PhotoImage(
			file = relative_to_assets("button_2.png"))
		self.button_2 = Button(
			image = self.button_image_2,
			command = lambda: self.play_screen.increase(),
			relief = "flat"
		)
		self.button_2.place(
			x = 86.0,
			y = 745.0,
			width = 85.0,
			height = 87.0
		)

		self.button_image_3 = PhotoImage(
			file = relative_to_assets("button_3.png"))
		self.button_3 = Button(
			image = self.button_image_3,
			command = lambda: print("button_3 clicked"),
			relief = "flat"
		)
		self.button_3.place(
			x = 171.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)

		self.button_image_4 = PhotoImage(
			file = relative_to_assets("button_4.png"))
		self.button_4 = Button(
			image = self.button_image_4,
			command = lambda:self.to_play_screen(),
			relief = "flat",
		)
		self.button_4.place(
			x = 342.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)

		self.button_image_5 = PhotoImage(
			file = relative_to_assets("button_5.png"))
		self.button_5 = Button(
			image = self.button_image_5,
			command = lambda: print("button_5 clicked"),
			relief = "flat"
		)
		self.button_5.place(
			x = 514.0,
			y = 745.0,
			width = 85.0,
			height = 87.0
		)

		self.button_image_6 = PhotoImage(
			file = relative_to_assets("button_6.png"))
		self.button_6 = Button(
			image = self.button_image_6,
			command = lambda: print("button_6 clicked"),
			relief = "flat"
		)
		self.button_6.place(
			x = 599.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)

		self.button_image_7 = PhotoImage(
			file = relative_to_assets("button_7.png"))
		self.button_7 = Button(
			image = self.button_image_7,
			command = lambda: print("button_7 clicked"),
			relief = "flat"
		)
		self.button_7.place(
			x = 770.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)

		self.button_image_8 = PhotoImage(
			file = relative_to_assets("button_8.png"))
		self.button_8 = Button(
			image = self.button_image_8,
			command = lambda: print("button_8 clicked"),
			relief = "flat"
		)
		self.button_8.place(
			x = 941.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)
		self.root.bind_all('<F5>', lambda event: self.button_4.invoke())
		self.root.bind_all('<F1>', lambda event: self.button_1.invoke())