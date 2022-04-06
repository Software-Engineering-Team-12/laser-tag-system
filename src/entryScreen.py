from tkinter import Canvas, Entry
import tkinter

class EntryScreen:
    	# Create Entry Screen
	def __init__(self, parent, view):
		self.red_team = {}
		self.green_team = {}
		self.window = tkinter.Frame(parent, bg='black')
		self.canvas = Canvas(
			self.window,
			bg = "#000000",
			height = view.WINDOW_HEIGHT,
			width = view.WINDOW_WIDTH,
			bd = 0,
			highlightthickness = 0,
			relief = "ridge"
		)
		self.canvas.pack()
		# Creates background rectangle for red team section
		self.canvas.create_rectangle(
			view.WINDOW_WIDTH * 0.1,
			view.WINDOW_HEIGHT * 0.0709,
			view.WINDOW_WIDTH / 2,
			view.WINDOW_HEIGHT * 0.8606,
			fill = "#330000",
			outline = ""
		)

		# Creates background rectangle for green team section
		self.canvas.create_rectangle(
			view.WINDOW_WIDTH / 2,
			view.WINDOW_HEIGHT * 0.0709,
			view.WINDOW_WIDTH * 0.9,
			view.WINDOW_HEIGHT * 0.8606,
			fill = "#003300",
			outline = ""
		)

		# Creates background rectangle for red team title
		self.canvas.create_rectangle(
			view.WINDOW_WIDTH * 0.215,
			view.WINDOW_HEIGHT * 0.07,
			view.WINDOW_WIDTH * 0.385,
			view.WINDOW_HEIGHT * 0.065 + view.WINDOW_WIDTH * 0.0292,
			outline = 'gray'
		)

		# Creates text for red team title
		self.canvas.create_text(
			view.WINDOW_WIDTH * 0.3,
			view.WINDOW_HEIGHT * 0.065,
			anchor = "n",
			text = "Red Team",
			fill = "#A29E9E",
			font = ("SegoeUI", -int(view.WINDOW_WIDTH * 0.0292)),
			justify="center"
		)

		# Creates background rectangle for green team title
		self.canvas.create_rectangle(
			view.WINDOW_WIDTH * 0.6,
			view.WINDOW_HEIGHT * 0.07,
			view.WINDOW_WIDTH * 0.8,
			view.WINDOW_HEIGHT * 0.065 + view.WINDOW_WIDTH * 0.0292,
			outline = 'gray'
		)

		# Creates text for green team title
		self.canvas.create_text(
			view.WINDOW_WIDTH * 0.7,
			view.WINDOW_HEIGHT * 0.065,
			anchor = "n",
			text = "Green Team",
			fill = "#A29E9E",
			font = ("SegoeUI", -int(view.WINDOW_WIDTH * 0.0292)),
			justify="center"
		)

		# Creates the text for the title of the screen
		self.canvas.create_text(
			view.WINDOW_WIDTH / 2,
			view.WINDOW_HEIGHT * 0.035,
			justify= "center",
			text = "Edit Current Game",
			fill = "#7F78D5",
			font = ("RobotoRoman Bold", -int(view.WINDOW_WIDTH * 0.0292))
		)

		# Creates background rectangle for the current game mode
		self.canvas.create_rectangle(
			view.WINDOW_WIDTH * 0.34761,
			view.WINDOW_HEIGHT * 0.86538,
			view.WINDOW_WIDTH * 0.65336 + 3,
			view.WINDOW_HEIGHT * 0.86538 + int(view.WINDOW_WIDTH * 0.01947),
			fill = "#C4C4C4",
			outline = "",
		)

		# Creates the text for the current game mode
		self.canvas.create_text(
			view.WINDOW_WIDTH * 0.34761,
			view.WINDOW_HEIGHT * 0.86538,
			anchor = "nw",
			text = "Game Mode: Standard public mode",
			fill = "#000000",
			font = ("SegoeUI", -int(view.WINDOW_WIDTH * 0.01947))
		)

		# Creates team entry height and width constants
		entry_width = view.WINDOW_WIDTH * 0.16553
		entry_height = view.WINDOW_HEIGHT * 0.02764
		codename_entry_offset = view.WINDOW_WIDTH * 0.17527
		# Loop to create player entry boxes for the both teams
		red_entry_x_pos = view.WINDOW_WIDTH * 0.13
		green_entry_x_pos = view.WINDOW_WIDTH * 0.53
		entry_y_pos = view.WINDOW_HEIGHT * 0.11178
		for i in range(20):
			# Creates entry for id of player for red team
			red_entry_id = Entry(self.window, textvariable = f'entry{i}')
			red_entry_id.place(
				x = red_entry_x_pos,
				y = entry_y_pos,
				width = entry_width,
				height = entry_height
			)
			# Creates entry for codename of player for red team
			red_entry_codename = Entry(self.window)
			red_entry_codename.place(
				x = red_entry_x_pos + codename_entry_offset,
				y = entry_y_pos,
				width = entry_width,
				height = entry_height
			)
			# Creates entry for id of player for green team
			green_entry_id = Entry(self.window)
			green_entry_id.place(
				x = green_entry_x_pos,
				y = entry_y_pos,
				width = entry_width,
				height = entry_height
			)
			# Creates entry for codename of player for green team
			green_entry_codename = Entry(self.window)
			green_entry_codename.place(
				x = green_entry_x_pos + codename_entry_offset,
				y = entry_y_pos,
				width = entry_width,
				height = entry_height
			)
			# Disable codename box initially
			red_entry_codename.config(state = "disabled")
			green_entry_codename.config(state = "disabled")
			# Creates entry number next to box for red team
			self.canvas.create_text(
				view.WINDOW_WIDTH * 0.1,
				entry_y_pos,
				anchor = "nw",
				text = f'{i:2}',
				fill = "#5F5E5E",
				font = ("SegoeUI", -int(entry_height))
			)
			# Creates entry number next to box for green team
			self.canvas.create_text(
				view.WINDOW_WIDTH / 2,
				entry_y_pos,
				anchor = "nw",
				text = f'{i:2}',
				fill = "#5F5E5E",
				font = ("SegoeUI", -int(entry_height))
			)
			# Add a bind to the entry box and codename box so when Tab is pressed it will query the id in the database and store new codename, id pair in database respectively
			red_entry_id.bind('<Tab>',lambda event, id = red_entry_id, name = red_entry_codename:view.controller.query_db(id, name, self.red_team))
			red_entry_codename.bind('<Tab>',lambda event, id = red_entry_id, name = red_entry_codename:view.controller.store_db(id, name, self.red_team))
			green_entry_id.bind('<Tab>',lambda event, id = green_entry_id, name = green_entry_codename:view.controller.query_db(id, name, self.green_team))
			green_entry_codename.bind('<Tab>',lambda event, id = green_entry_id, name = green_entry_codename:view.controller.store_db(id, name, self.green_team))
			entry_y_pos += view.WINDOW_HEIGHT * 0.037
		