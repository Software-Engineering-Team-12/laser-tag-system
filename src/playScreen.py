
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./gui_assets")

"""
TODO
replace 0:00 with timer function to countdown
figure out placing names with scores
reorder names based on score

"""
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
class PlayScreen:

    def __init__(self):
        self.createWindow()
    # TEMP METHOD: assigned to button 1 for now to test increasing teams total value
    def increase(self):
        self.red["codename1"] += 1000
        self.green["codename1"] += 1000

    def update_score(self,):
            red_scores = 0
            green_scores = 0
            for x in self.red:
                red_scores += self.red[x]
            for x in self.green:
                green_scores += self.green[x]
            self.red_total.set(max(red_scores,self.red_total.get()))
            self.green_total.set(max(green_scores,self.green_total.get()))
            self.window.after(100,self.update_score)

    def createWindow(self):
        self.red = {
            "codename1": 1000,
            "codename2": 0}
        self.green = {
            "codename1": 1000,
            "codename2": 0}

        self.window = Tk()

        self.red_total = IntVar(self.window, value=0)
        self.green_total= IntVar(self.window, value=0)
            
        self.window.geometry("1027x832")
        self.window.configure(bg = "#000000")


        self.canvas = Canvas(
            self.window,
            bg = "#000000",
            height = 832,
            width = 1027,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.increase(),
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=745.0,
            width=86.0,
            height=87.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=86.0,
            y=745.0,
            width=85.0,
            height=87.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=171.0,
            y=745.0,
            width=86.0,
            height=87.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=342.0,
            y=745.0,
            width=86.0,
            height=87.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=514.0,
            y=745.0,
            width=85.0,
            height=87.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=599.0,
            y=745.0,
            width=86.0,
            height=87.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=770.0,
            y=745.0,
            width=86.0,
            height=87.0
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=941.0,
            y=745.0,
            width=86.0,
            height=87.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            513.0,
            365.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            795.0,
            635.0,
            anchor="nw",
            text="0:00",
            fill="#FFFFFF",
            font=("RobotoRoman Bold", 30 * -1)
        )

        self.canvas.create_text(
            549.0,
            633.0,
            anchor="nw",
            text="Time Remaining:",
            fill="#FFFFFF",
            font=("RobotoRoman Bold", 30 * -1)
        )

        self.red_team_total = Entry(
            bd=0,
            bg="#000000",
            fg="red",
            font="SegoeUI 20",
            readonlybackground="black",
            highlightthickness=0,
            textvariable=self.red_total
        )
        self.red_team_total.config(state="readonly")
        self.red_team_total.place(
            x=422.0,
            y=318.0,
            width=91.0,
            height=29.0
        )

        self.green_team_total = Entry(
            bd=0,
            bg="#000000",
            fg="green",
            font="SegoeUI 20",
            readonlybackground="black",
            highlightthickness=0,
            textvariable=self.green_total
        )
        self.green_team_total.config(state="readonly")
        self.green_team_total.place(
            x=812.0,
            y=318.0,
            width=91.0,
            height=29.0
        )

        self.action_display = Text(
            bd=0,
            bg="#0E2B56",
            fg="white",
            font="SegoeUI 20",
            highlightthickness=0
        )
        self.action_display.place(
            x=142.0,
            y=382.0,
            width=372.0,
            height=230.0
        )

        self.red_team_scores = Text(
            bd=0,
            bg="#000000",
            fg="red",
            font="SegoeUI 20",
            highlightthickness=0
        )
        self.red_team_scores.place(
            x=130.0,
            y=108.0,
            width=383.0,
            height=208.0
        )

        self.green_team_scores = Text(
            bd=0,
            bg="#000000",
            fg="green",
            font="SegoeUI 20",
            highlightthickness=0
        )
        self.green_team_scores.place(
            x=518.0,
            y=108.0,
            width=383.0,
            height=208.0
        )
        self.window.resizable(False, False)
        
screen = PlayScreen()
screen.update_score()
screen.window.mainloop()
 