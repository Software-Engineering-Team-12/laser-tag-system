from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./gui_assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class View:

	# Default constructor
	def __init__(self):
		self.entryScreen()
		
	# Create Entry Screen
	def entryScreen(self):
		window = Tk()
		window.geometry("1027x832")
		window.configure(bg = "#000000")
		window.title('Player Entry Screen')
		canvas = Canvas(
			window,
			bg = "#000000",
			height = 900,
			width = 1000,
			bd = 0,
			highlightthickness = 0,
			relief = "ridge"
		)

		canvas.place(x = 0, y = 0)
		#creates background rectangle for red team section
		canvas.create_rectangle(
			100.0,
			59.0,
			500.0,
			716.0,
			fill = "#330000",
			outline = ""
		)

		#creates background rectangle for green team section
		canvas.create_rectangle(
			500.0,
			59.0,
			900.0,
			716.0,
			fill = "#003300",
			outline = ""
		)

		#creates background rectangle for red team title
		canvas.create_rectangle(
			229.0,
			61.0,
			372.0,
			89.0,
			fill = "#330000",
			outline = 'gray'
		)

		#creates text for red team title
		canvas.create_text(
			231.0,
			58.0,
			anchor = "nw",
			text = "Red Team",
			fill = "#A29E9E",
			font = ("SegoeUI", 30 * -1)
		)

		#creates background rectangle for green team title
		canvas.create_rectangle(
			615.0,
			61.0,
			785.0,
			89.0,
			fill = "#003300",
			outline = 'gray'
		)

		#creates text for green team title
		canvas.create_text(
			617.0,
			58.0,
			anchor = "nw",
			text = "Green Team",
			fill = "#A29E9E",
			font = ("SegoeUI", 30 * -1)
		)

		#creates the text for the title of the screen
		canvas.create_text(
			382.0,
			13.0,
			anchor = "nw",
			text = "Edit Current Game",
			fill = "#7F78D5",
			font = ("RobotoRoman Bold", 30 * -1)
		)

		#creates background rectangle for the current game mode
		canvas.create_rectangle(
			357.0,
			720.0,
			671.0,
			741.0,
			fill = "#C4C4C4",
			outline = ""
		)

		#creates the text for the current game mode
		canvas.create_text(
			357.0,
			718.0,
			anchor = "nw",
			text = "Game Mode: Standard public mode",
			fill = "#000000",
			font = ("SegoeUI", 20 * -1)
		)

		#method to add all of the entries to arrays for storage
		def gatherEntries():
			red_entries = []
			green_entries = []
			for n in range(20):
				red_id = red_entries_id[n].get()
				red_codename = red_entries_codename[n].get()
				green_id = green_entries_id[n].get()
				green_codename = green_entries_codename[n].get()
				red_dict = {"id": red_id, "codename": red_codename}
				green_dict = {"id": green_id, "codename": green_codename}
				red_entries.append(red_dict)
				green_entries.append(green_dict)
			print(red_entries)
			print(green_entries)

		#creates team entry height and width constants
		entry_width = 170.0
		entry_heigh = 23.0
		codename_entry_offset = 180.0
		#loop to create player entry boxes for the red team
		red_entries_id = []
		red_entries_codename = []
		red_entry_x_pos = 132.0
		red_entry_y_pos = 93.0
		for i in range(20):
			#creates entry for id of player for red team
			entry_id = Entry(window)
			entry_id.place(
				x = red_entry_x_pos,
				y = red_entry_y_pos,
				width = entry_width,
				height = entry_heigh
			)
			#creates entry for codename of player for red team
			entry_codename = Entry(window)
			entry_codename.place(
				x = red_entry_x_pos + codename_entry_offset,
				y = red_entry_y_pos,
				width = entry_width,
				height = entry_heigh
			)
			#creates entry number next to box for red team
			canvas.create_text(
				104.0,
				red_entry_y_pos,
				anchor = "nw",
				text = f'{i:2}',
				fill = "#5F5E5E",
				font = ("SegoeUI", 20 * -1)
			)
			#adds entry to array and increases the y pos of next entry
			red_entries_id.append(entry_id)
			red_entries_codename.append(entry_codename)
			red_entry_y_pos += 31.0

		#loop to create entry boxes for the green team
		green_entries_id = []
		green_entries_codename = []
		green_entry_x_pos = 532.0
		green_entry_y_pos = 93.0
		for j in range(20):
			#creates entry for id of player for green team
			entry_id = Entry(window)
			entry_id.place(
				x = green_entry_x_pos,
				y = green_entry_y_pos,
				width = entry_width,
				height = entry_heigh
			)
			#creates entry for codename of player for green team
			entry_codename = Entry(window)
			entry_codename.place(
				x = green_entry_x_pos + codename_entry_offset,
				y = green_entry_y_pos,
				width = entry_width,
				height = entry_heigh
			)
			#creates entry number next to box for green team
			canvas.create_text(
				504.0,
				green_entry_y_pos,
				anchor = "nw",
				text = f'{j:2}',
				fill = "#5F5E5E",
				font = ("SegoeUI", 20 * -1)
			)
			#adds entry array and increases the y pos of next entry
			green_entries_id.append(entry_id)
			green_entries_codename.append(entry_codename)
			green_entry_y_pos += 31.0

		#code below creates all of the buttons at the bottom of the window (8 buttons in total)
		button_image_1 = PhotoImage(
			file = relative_to_assets("button_1.png"))
		button_1 = Button(
			image = button_image_1,
			command = lambda: print("button_1 clicked"),
			relief = "flat"
		)
		button_1.place(
			x = 0.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)

		button_image_2 = PhotoImage(
			file = relative_to_assets("button_2.png"))
		button_2 = Button(
			image = button_image_2,
			command = lambda: print("button_2 clicked"),
			relief = "flat"
		)
		button_2.place(
			x = 86.0,
			y = 745.0,
			width = 85.0,
			height = 87.0
		)

		button_image_3 = PhotoImage(
			file = relative_to_assets("button_3.png"))
		button_3 = Button(
			image = button_image_3,
			command = lambda: print("button_3 clicked"),
			relief = "flat"
		)
		button_3.place(
			x = 171.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)

		button_image_4 = PhotoImage(
			file = relative_to_assets("button_4.png"))
		button_4 = Button(
			image = button_image_4,
			command = lambda: print("button_4 clicked"),
			relief = "flat"
		)
		button_4.place(
			x = 342.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)

		button_image_5 = PhotoImage(
			file = relative_to_assets("button_5.png"))
		button_5 = Button(
			image = button_image_5,
			command = gatherEntries,
			relief = "flat"
		)
		button_5.place(
			x = 514.0,
			y = 745.0,
			width = 85.0,
			height = 87.0
		)

		button_image_6 = PhotoImage(
			file = relative_to_assets("button_6.png"))
		button_6 = Button(
			image = button_image_6,
			command = lambda: print("button_6 clicked"),
			relief = "flat"
		)
		button_6.place(
			x = 599.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)

		button_image_7 = PhotoImage(
			file = relative_to_assets("button_7.png"))
		button_7 = Button(
			image = button_image_7,
			command = lambda: print("button_7 clicked"),
			relief = "flat"
		)
		button_7.place(
			x = 770.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)

		button_image_8 = PhotoImage(
			file = relative_to_assets("button_8.png"))
		button_8 = Button(
			image = button_image_8,
			command = lambda: print("button_8 clicked"),
			relief = "flat"
		)
		button_8.place(
			x = 941.0,
			y = 745.0,
			width = 86.0,
			height = 87.0
		)
		window.resizable(False, False)
		window.mainloop()

