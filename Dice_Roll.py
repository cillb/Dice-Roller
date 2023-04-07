"""
This is a simple class containing a function to simulate dice rolls, 
using the random.randint module.
The dice roll can simulate any amount of rolls for a single size of die
(eg 6-sided, 20-sided, etc.)
It is called as part of the Dice_Roller app's roll function.
"""
from random import randint as r

class Dice_Roll:
    def __init__(self):
        self.total = 0

    def rolling(self, number_of_rolls, type_of_dice):
        roll = [str(r(1, type_of_dice)) for i in range(number_of_rolls)]
        for x in roll:
            self.total += int(x)
        return roll