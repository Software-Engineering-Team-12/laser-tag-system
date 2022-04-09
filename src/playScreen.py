from pathlib import Path
import time
from tkinter import *
import tkinter
from .socket import gameSocket
from .traffic_generator import trafficGenerator


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./gui_assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
class PlayScreen:

    def __init__(self, parent, entry_screen, view):
        self.startTime = time.time()
        self.view = view
        self.create_window(parent, entry_screen, view)
        self.change_time()
        self.game_Socket = gameSocket(self)
        self.game_Socket.start()
        self.traffic = trafficGenerator()
        self.traffic.set_teams(self.red_players,self.green_players)
    # TEMP METHOD: assigned to button 1 for now to test increasing teams total value for testing
    def increase(self):
        for key1,key2 in zip(self.red_players,self.green_players):
            self.red_players[key1] += 800
            self.green_players[key2] += 900

    def update_action_log(self, message):
        # insert action to text box
        self.action_display.insert(END, f'{message.replace(":", " hit ")}\n')
        self.action_display.see(END)
        # increment score of leading player
        lead = message.split(":")[0]
        if lead in self.red_players:
            self.red_players[lead] += 100
        else:
            self.green_players[lead] += 100

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
                    textbox.insert(END, f'{k:27}{v:6}\n')
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
        # if team totals are equal keep team colors solid with no flashing
        elif self.green_team_total.get() == self.red_team_total.get():
            self.green_team_total.config(fg = "green")
            self.red_team_total.config(fg = "red")
    
    def change_time(self):
        # calculates current time that remains
        self.timeLeft = int(391-(time.time() - self.startTime))
        # stop timer when time is up
        if self.timeLeft <= 0:
            self.canvas.itemconfig(self.warning_time, text = f'Times up!')
            self.canvas.itemconfig(self.countdown, text = f'Time Remaining: 0:00')
            if self.red_total.get() > self.green_total.get():
                self.view.to_result_screen("Red")
            elif self.green_total.get() > self.red_total.get():
                self.view.to_result_screen("Green")
            else:
                self.view.to_result_screen("Tie")
        else:
            # show warning timer first
            if self.timeLeft > 360:
                self.minutes = int((self.timeLeft-360)/60)
                self.seconds = self.timeLeft%60
                self.canvas.itemconfig(self.countdown, text = f'Game Starting in: {self.minutes:02}:{self.seconds:02}')
            # stops counting down if time is up
            elif self.timeLeft != 0:
                if not self.traffic.running:
                    self.traffic.start()
                self.minutes = int(self.timeLeft/60)
                self.seconds = self.timeLeft%60
                self.canvas.itemconfig(self.countdown, text = f'Time Remaining: {self.minutes:02}:{self.seconds:02}')

                if(self.timeLeft == 180):
                    self.canvas.itemconfig(self.warning_time, text = f'Warning 3 minutes left!')
                elif (self.timeLeft == 60):
                    self.canvas.itemconfig(self.warning_time, text = f'Warning 1 minutes left!')
                elif (self.timeLeft == 30):
                    self.canvas.itemconfig(self.warning_time, text = f'Warning 30 seconds left!')
            self.window.after(1000, self.change_time)



    def create_window(self, parent, entry_screen, view):
        # set team dictionaries from entry screen
        self.red_players = entry_screen.red_team.copy()
        self.green_players = entry_screen.green_team.copy()
        # create screen
        self.window = tkinter.Frame(parent)
        self.window.configure(bg = "#000000")
        # initialize team totals
        self.red_total = IntVar(self.window, value=0)
        self.green_total= IntVar(self.window, value=0)
        # initialize canvas
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
        
        # create and place UI
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            view.WINDOW_WIDTH / 2,
            view.WINDOW_HEIGHT * 0.45,
            image=self.image_image_1,
        )

        # create and place timer 
        self.countdown = self.canvas.create_text(
            view.WINDOW_WIDTH * 0.53,
            view.WINDOW_HEIGHT * 0.8,
            anchor="nw",
            text="Time Remaining: 0:00",
            fill="#FFFFFF",
            font=("RobotoRoman Bold", 30 * -1)
        )

        # create and place warning message
        self.warning_time = self.canvas.create_text(
            view.WINDOW_WIDTH * 0.136,
            view.WINDOW_HEIGHT * 0.8,
            anchor = "nw",
            text = "",
            fill = "#FFFFFF",
            font = ("RobotoRoman Bold", 30 * -1)
        )

        # create and place red team's total score box
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
            x=view.WINDOW_WIDTH * 0.498,
            y=view.WINDOW_HEIGHT * 0.4,
            width=91.0,
            height=29.0,
            anchor="e"
        )

        # create and place red team's scoreboard
        self.red_team_scores = Text(
            self.window,
            bd=0,
            bg="black",
            fg="red",
            font="SegoeUI 20",
            highlightthickness=0,
            state="disabled"
        )
        self.red_team_scores.place(
            x=view.WINDOW_WIDTH * 0.1,
            y=view.WINDOW_HEIGHT * 0.11,
            width=383.0,
            height=208.0
        )

        # create and place green team's total score box
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
            x=view.WINDOW_WIDTH * 0.898,
            y=view.WINDOW_HEIGHT * 0.4,
            width=91.0,
            height=29.0,
            anchor="e"
        )

        # create and place green team's scoreboard
        self.green_team_scores = Text(
            self.window,
            bd=0,
            bg="black",
            fg="green",
            font="SegoeUI 20",
            highlightthickness=0,
            state="disabled",
        )
        self.green_team_scores.place(
            x=view.WINDOW_WIDTH * 0.5,
            y=view.WINDOW_HEIGHT * 0.11,
            width=383.0,
            height=208.0
        )

        # create and place action log box
        self.action_display = Text(
            self.window,
            bd=0,
            bg="#0E2B56",
            fg="white",
            font="SegoeUI 20",
            highlightthickness=0
        )
        self.action_display.place(
            x=view.WINDOW_WIDTH * 0.499,
            y=view.WINDOW_HEIGHT * 0.46,
            width=372.0,
            height=230.0,
            anchor="ne"
        )
        
