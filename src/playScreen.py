from pathlib import Path
import time
from tkinter import *
import tkinter


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./gui_assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
class PlayScreen:

    def __init__(self, parent, entry_screen):
        self.startTime = time.time()
        self.create_window(parent, entry_screen)
        self.change_time()
    # TEMP METHOD: assigned to button 1 for now to test increasing teams total value for testing
    def increase(self):
        for key1,key2 in zip(self.red_players,self.green_players):
            self.red_players[key1] += 800
            self.green_players[key2] += 900

    def update_score(self):
            # creates a sorted list from each team's dictionary
            red_sorted = sorted(self.red_players.items(), key=lambda x:x[1], reverse=TRUE)
            green_sorted = sorted(self.green_players.items(), key=lambda x:x[1], reverse=TRUE)

            # iterate through each teams textbox and sorted list together
            for textbox, lst in {self.red_team_scores:red_sorted, self.green_team_scores:green_sorted}.items():
                # set textbox to normal for editing
                textbox.config(state="normal")
                # remove previous text
                textbox.delete(1.0, END)
                # insert new scoreboard
                for k,v in lst:
                    textbox.insert(END, f'{k:26}{v:6}\n')
                # close scoreboard again so no editing can be done
                textbox.config(state="disabled")

            # start totals
            red_scores = 0
            green_scores = 0
            # calculate new total score
            for i in self.red_players:
                red_scores += self.red_players[i]
            for j in self.green_players:
                green_scores += self.green_players[j]
            # set new total
            self.red_total.set(max(red_scores,self.red_total.get()))
            self.green_total.set(max(green_scores,self.green_total.get()))
            # flash leading score
            self.flash_score()
            # tkinters way of running this again after specified time
            self.window.after(100,self.update_score)
    
    # method to flash the score of the team with highest score
    def flash_score(self):
        # checks if red team score is greater than green team
        if self.red_total.get() > self.green_total.get():
            # gets the current color of the team total score text
            self.current_color = self.red_team_total.cget("fg")
            # sets the next color of the text
            self.next_color = "black" if self.current_color == "red" else "red"
            # assigns the next color to the entry text color
            self.red_team_total.config(fg = self.next_color)
        # checks if green team score is greater than red team
        elif self.green_total.get() > self.red_total.get():
            self.current_color = self.green_team_total.cget("fg")
            self.next_color = "black" if self.current_color == "green" else "green"
            self.green_team_total.config(fg = self.next_color)
    
    def change_time(self):
        # calculates current time that remains
        self.timeLeft = int(391-(time.time() - self.startTime))
        # show warning timer first
        if self.timeLeft > 360:
            self.minutes = int((self.timeLeft-360)/60)
            self.seconds = self.timeLeft%60
            self.canvas.itemconfig(self.countdown, text = f'Game Starting in: {self.minutes:02}:{self.seconds:02}')
        # stops counting down if time is up
        else:
            self.minutes = int(self.timeLeft/60)
            self.seconds = self.timeLeft%60
            self.canvas.itemconfig(self.countdown, text = f'Time Remaining: {self.minutes:02}:{self.seconds:02}')

            if(self.timeLeft == 180):
                self.canvas.itemconfig(self.warning_time, text = f'Warning 3 minutes left')
            elif (self.timeLeft == 60):
                self.canvas.itemconfig(self.warning_time, text = f'Warning 1 minutes left')
            elif (self.timeLeft == 30):
                self.canvas.itemconfig(self.warning_time, text = f'Warning 30 minutes left')
            elif (self.timeLeft == 0):
                self.canvas.itemconfig(self.warning_time, text = f'End of time')
        self.window.after(1000, self.change_time)


    def create_window(self, parent, entry_screen):
        self.red_players = entry_screen.red_team
        self.green_players = entry_screen.green_team

        self.window = tkinter.Frame(parent)
        self.window.configure(bg = "#000000")
        self.red_total = IntVar(self.window, value=0)
        self.green_total= IntVar(self.window, value=0)
        
        self.canvas = Canvas(
            self.window,
            bg = "#000000",
            height = 747,
            width = 1027,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.pack()

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            513.0,
            365.0,
            image=self.image_image_1
        )

        self.countdown = self.canvas.create_text(
            549.0,
            630.0,
            anchor="nw",
            text="Time Remaining: 0:00",
            fill="#FFFFFF",
            font=("RobotoRoman Bold", 30 * -1)
        )

        self.warning_time = self.canvas.create_text(
            140.0,
            630.0,
            anchor = "nw",
            text = "",
            fill = "#FFFFFF",
            font = ("RobotoRoman Bold", 30 * -1)
        )

        # self.time_text = self.canvas.create_text(
        #     549.0,
        #     633.0,
        #     anchor="nw",
        #     text="Time Remaining:",
        #     fill="#FFFFFF",
        #     font=("RobotoRoman Bold", 30 * -1)
        # )

        self.red_team_total = Entry(
            self.window,
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
            self.window,
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
            self.window,
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
            self.window,
            bd=0,
            bg="#000000",
            fg="red",
            font="SegoeUI 20",
            highlightthickness=0,
            state="disabled"
        )
        self.red_team_scores.place(
            x=130.0,
            y=108.0,
            width=383.0,
            height=208.0
        )

        self.green_team_scores = Text(
            self.window,
            bd=0,
            bg="#000000",
            fg="green",
            font="SegoeUI 20",
            highlightthickness=0,
            state="disabled"
        )
        self.green_team_scores.place(
            x=518.0,
            y=108.0,
            width=383.0,
            height=208.0
        )
        
