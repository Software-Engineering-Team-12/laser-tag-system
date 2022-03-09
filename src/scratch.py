# from tkinter import *
 
# root = Tk()
# root.geometry("300x300")
# root.title(" Q&A ")
 
# def Take_input():
#     INPUT = inputtxt.get("1.0", "end-1c")
#     print(INPUT)
#     if(INPUT == "120"):
#         Output.config(state="normal")
#         Output.delete(1.0,END)
#         Output.insert(END, 'Correct')
#         Output.config(state="disabled")
#     else:
#         Output.config(state="normal")
#         Output.delete(1.0,END)
#         Output.insert(END, "Wrong answer")
#         Output.config(state="disabled")
     
# l = Label(text = "What is 24 * 5 ? ")
# inputtxt = Text(root, height = 10,
#                 width = 25,
#                 bg = "light yellow")
 
# Output = Text(root, height = 5,
#               width = 25,
#               bg = "light cyan",
#               state= "disabled")
 
# Display = Button(root, height = 2,
#                  width = 20,
#                  text ="Show",
#                  command = lambda:Take_input())
 
# l.pack()
# inputtxt.pack()
# Display.pack()
# Output.pack()
 
# mainloop()
redscores = 0
greenscores = 1
red = {
            "codename1": 1000,
            "codename2": 0}
green = {
    "codename1": 1000,
    "codename2": 0}

for textbox, dict in {redscores:red, greenscores:green}.items():
    print(textbox)
    for k,v in dict.items():
        print( k)
        print( v)