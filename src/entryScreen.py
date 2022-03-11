from pathlib import Path
# Explicit imports to satisfy Flake8
from tkinter import Canvas, Entry, Button, PhotoImage
import tkinter
from .playScreen import PlayScreen

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./gui_assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class EntryScreen:
    	# Create Entry Screen
	def __init__(self, parent, view):
		self.window = tkinter.Frame(parent, bg='black')
		self.canvas = Canvas(
			self.window,
			bg = "#000000",
			height = 747,
			width = 1000,
			bd = 0,
			highlightthickness = 0,
			relief = "ridge"
		)

		self.canvas.pack()
		# Creates background rectangle for red team section
		self.canvas.create_rectangle(
			100.0,
			59.0,
			500.0,
			716.0,
			fill = "#330000",
			outline = ""
		)

		# Creates background rectangle for green team section
		self.canvas.create_rectangle(
			500.0,
			59.0,
			900.0,
			716.0,
			fill = "#003300",
			outline = ""
		)

		# Creates background rectangle for red team title
		self.canvas.create_rectangle(
			229.0,
			61.0,
			372.0,
			89.0,
			fill = "#330000",
			outline = 'gray'
		)

		# Creates text for red team title
		self.canvas.create_text(
			231.0,
			58.0,
			anchor = "nw",
			text = "Red Team",
			fill = "#A29E9E",
			font = ("SegoeUI", 30 * -1)
		)

		# Creates background rectangle for green team title
		self.canvas.create_rectangle(
			615.0,
			61.0,
			785.0,
			89.0,
			fill = "#003300",
			outline = 'gray'
		)

		# Creates text for green team title
		self.canvas.create_text(
			617.0,
			58.0,
			anchor = "nw",
			text = "Green Team",
			fill = "#A29E9E",
			font = ("SegoeUI", 30 * -1)
		)

		# Creates the text for the title of the screen
		self.canvas.create_text(
			382.0,
			13.0,
			anchor = "nw",
			text = "Edit Current Game",
			fill = "#7F78D5",
			font = ("RobotoRoman Bold", 30 * -1)
		)

		# Creates background rectangle for the current game mode
		self.canvas.create_rectangle(
			357.0,
			720.0,
			671.0,
			741.0,
			fill = "#C4C4C4",
			outline = ""
		)

		# Creates the text for the current game mode
		self.canvas.create_text(
			357.0,
			718.0,
			anchor = "nw",
			text = "Game Mode: Standard public mode",
			fill = "#000000",
			font = ("SegoeUI", 20 * -1)
		)

		# Creates team entry height and width constants
		entry_width = 170.0
		entry_height = 23.0
		codename_entry_offset = 180.0
		# Loop to create player entry boxes for the red team
		# self.red_entries_id = []
		# self.red_entries_codename = []
		red_entry_x_pos = 132.0
		red_entry_y_pos = 93.0
		for i in range(20):
			# Creates entry for id of player for red team
			entry_id = Entry(self.window, textvariable = f'entry{i}')
			entry_id.place(
				x = red_entry_x_pos,
				y = red_entry_y_pos,
				width = entry_width,
				height = entry_height
			)
			# Creates entry for codename of player for red team
			entry_codename = Entry(self.window)
			entry_codename.place(
				x = red_entry_x_pos + codename_entry_offset,
				y = red_entry_y_pos,
				width = entry_width,
				height = entry_height
			)
			# Disable codename box initially
			entry_codename.config(state = "disabled")
			# Creates entry number next to box for red team
			self.canvas.create_text(
				104.0,
				red_entry_y_pos,
				anchor = "nw",
				text = f'{i:2}',
				fill = "#5F5E5E",
				font = ("SegoeUI", 20 * -1)
			)
			# Add a bind to the entry box and codename box so when Tab is pressed it will query the id in the database and store new codename, id pair in database respectively
			entry_id.bind('<Tab>',lambda event, id = entry_id, name = entry_codename:view.controller.query_db(id, name))
			entry_codename.bind('<Tab>',lambda event, id = entry_id, name = entry_codename:view.controller.store_db(id, name))
			# Adds entry to array and increases the y pos of next entry
			# self.red_entries_id.append(entry_id)
			# self.red_entries_codename.append(entry_codename)
			red_entry_y_pos += 31.0

		# Loop to create entry boxes for the green team
		# self.green_entries_id = []
		# self.green_entries_codename = []
		green_entry_x_pos = 532.0
		green_entry_y_pos = 93.0
		for j in range(20):
			# Creates entry for id of player for green team
			entry_id = Entry(self.window)
			entry_id.place(
				x = green_entry_x_pos,
				y = green_entry_y_pos,
				width = entry_width,
				height = entry_height
			)
			# Creates entry for codename of player for green team
			entry_codename = Entry(self.window)
			entry_codename.place(
				x = green_entry_x_pos + codename_entry_offset,
				y = green_entry_y_pos,
				width = entry_width,
				height = entry_height
			)
			# Disable codename box initially
			entry_codename.config(state = "disabled")
			# Creates entry number next to box for green team
			self.canvas.create_text(
				504.0,
				green_entry_y_pos,
				anchor = "nw",
				text = f'{j:2}',
				fill = "#5F5E5E",
				font = ("SegoeUI", 20 * -1)
			)
			# Add a bind to the entry box and codename box so when Tab is pressed it will query the id in the database and store new codename, id pair in database respectively
			entry_id.bind('<Tab>',lambda event, id = entry_id, name = entry_codename:view.controller.query_db(id, name))
			entry_codename.bind('<Tab>',lambda event, id = entry_id, name = entry_codename:view.controller.store_db(id, name))
			#adds entry array and increases the y pos of next entry
			# self.green_entries_id.append(entry_id)
			# self.green_entries_codename.append(entry_codename)
			green_entry_y_pos += 31.0

		# Code below creates all of the buttons at the bottom of the window (8 buttons in total)
		self.button_image_1 = PhotoImage(
			file = relative_to_assets("button_1.png"))
		self.button_1 = Button(
			image = self.button_image_1,
			command = lambda: view.to_entry_screen(),
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
			command = lambda: PlayScreen.increase(view.play_screen),
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
			command = lambda: view.to_play_screen(),
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