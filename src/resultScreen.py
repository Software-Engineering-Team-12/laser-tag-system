from pathlib import Path
from tkinter import *
import tkinter

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./gui_assets")

def relative_to_assets(path: str) -> Path:
	return ASSETS_PATH / Path(path)
class ResultScreen:

	def __init__(self, parent, entry_screen, view, winner):
		self.create_window(parent, entry_screen, view, winner)

	def create_window(self, parent, entry_screen, view, winner):
		self.window = tkinter.Frame(parent)
		self.window.configure(bg = "#000000")
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
		if winner == "Tie":
			self.winMessage = Label(
			self.window,
			bd=0,
			fg="yellow",
			bg = "#000000",
			font="SegoeUI 20",
			text="A tie!"
			)
		else:
			self.winMessage = Label(
				self.window,
				bd=0,
				fg=winner,
				bg = "#000000",
				font="SegoeUI 20",
				text= winner + " Team Wins!"
			)
		self.winMessage.pack()
		self.winMessage.place(
			x=view.WINDOW_WIDTH * 0.600,
			y=view.WINDOW_HEIGHT * 0.4,
			width=220.0,
			height=29.0,
			anchor="e"
		)