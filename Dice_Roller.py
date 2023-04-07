"""
This python code creates an app used to make dice rolls. The GUI is made with tkinter,
and has two fields for entry; The size of die being rolled, and the number being rolled.
The individual rolls are displayed along with the total number rolled.
The accompanying Dice_Roll module is imported, and carries out the actual dice roll function.
"""
from tkinter import *
from tkinter import font
from Dice_Roll import *
# the class App is created, it fills out everything inside the app
class App:
    def __init__(self, master):
        self.d_roll = Dice_Roll()# the Dice_Roll module is initialised for the app
        frame = Frame(master)
        frame.pack()
        # set a font format
        font_style = font.Font(family="Calibri", size=12)
        self.number_dice = IntVar()#    the number of dice to roll
        self.dice_rolled = IntVar()#    the type of dice to roll
        self.rolled_dice = StringVar()# the result of each dice rolled
        self.total_rolled = IntVar()#   the total of all the dice rolled
        # the entry fields to define the dice roll are defined
        Label(frame, text="Number of Dice", font=font_style).grid(row=0, column=0, sticky="W")
        Entry(frame, textvariable=self.number_dice, width=10, font=font_style).grid(row=0, column=1, padx=5, sticky="W")
        Label(frame, text="Type of Dice", font=font_style).grid(row=1, column=0, sticky="W")
        Entry(frame, textvariable=self.dice_rolled, width=10, font=font_style).grid(row=1, column=1)
        # the results fields are created
        Label(frame, text="Dice", font=font_style).grid(row=3, column=1, sticky="E")
        Label(frame, textvariable=self.rolled_dice, justify="left", background="white", borderwidth=1, relief="sunken", width=15, wraplength=120, font=font_style).grid(row=3, column=2, padx=5)
        Label(frame, text="Total", font=font_style).grid(row=2, column=1, sticky="E")
        Label(frame, textvariable=self.total_rolled, anchor="w", background="white", borderwidth=1, relief="sunken", width=5, font=font_style).grid(row=2, column=2, padx=5, sticky=W)
        button = Button(frame, text="ROLL", command= self.roll, width=10, background="#e6e6e6", activebackground="#4da6ff", activeforeground="white", font=font_style)
        button.grid(row=2, column=0, pady=10)
    # the function to roll the dice using the Dice_Roll module is set up here
    # it writes the results and total to the rolled_dice and total_rolled
    def roll(self):
        self.d_roll.total = 0
        number = self.number_dice.get()
        dice = self.dice_rolled.get()
        self.rolled_dice.set(self.d_roll.rolling(int(number), int(dice)))
        self.total_rolled.set(self.d_roll.total)
# the app is created, named, dimensioned and assigned the class above
root = Tk()
root.wm_title("Dice Roller")
root.geometry("400x150")
app = App(root)
root.mainloop()
