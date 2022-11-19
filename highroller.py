"""
Name: Student
Date: 11/18/22
Description: High Roller
"""

from random import randint
from sys import exit


class Die():
    """
    A simple class for representing die objects. A die has a given number of
    sides (at least) four, set when the die is constructed and which can never
    be changed. The die's value can be changed, but only by calling its roll()
    method.
    """

    def __init__(self, initial_value, sides):
        """
        Constructs a new Die object with two attributes:
        - self.value: starting value of the die, given by parameter initial_value
        - self.sides: number of sides of the die, given by parameter sides
        """
        self.value = None  # TODO: set the value of this die
        self.sides = None  # TODO: set the number of sides

    def roll(self):
        """
        Simulates a roll by randomly updating the value of this die.
        In addition to mutating the die's value, this method also
        returns the new updated value.
        """
        pass

    def get_number_sides(self):
        """
        Returns the number of sides of this die.
        """
        pass

    def get_current_value(self):
        """
        Returns the current value of this die.
        """
        pass

    def __str__(self):
        """
        Returns a string representation of this die, which is its value enclosed in square
        brackets, without spaces, for example "[5]".
        """
        pass


class DiceSet():
    """
    A dice set holds a collection of Die objects. All of the die objects have
    the same number of sides. 
    """

    def __init__(self, sides_each_die, number_of_dice):
        """
        Creates a new DiceSet. This constructor should initialize the following attributes:
        - self.dice: a list of Die objects, each with the given number of sides
        """
        self.dice = None  # TODO: create a list of dice with the given number of sides and number of dice

    def get_descriptor(self):
        """
        Returns the descriptor of the dice set; for example "5d20" for a set with
        five dice of 20 sides each; or "2d6" for a set of two six-sided dice.
        """
        pass

    def get_total(self):
        """
        Returns the total of the values of each die in the set.
        """
        pass

    def roll_all(self):
        """
        Rolls all of the dice in the set, and returns the total of the new values.
        """
        pass

    def roll_die(self, i):
        """
        Rolls the die at the given index in the set, and returns the new value.
        """
        pass

    def get_current_values(self):
        """
        Returns a list of the current values of each die in the set.
        """
        pass

    def matches(self, dice_set):
        """
        Returns whether this dice set has the same distribution of values as
        another dice set. The two dice sets must have the same number of dice
        and the same number of sides per dice, and there must be the same
        number of each value in each set.
        """
        pass

    def __str__(self):
        """
        Returns a string representation in which each of the die strings are
        joined without a separator, for example: "[2][5][2][3]".
        """
        pass


class HighRollerGame():
    """
    A HighRollerGame object represents a single game of High Roller.
    It maintains the current dice set and (optionally) the highest total so far.
    """

    def __init__(self):
        """
        Creates a new HighRollerGame. This constructor should initialize the following attributes:
        - self.dice_set: a DiceSet containing 5 dice with 6 sides each
        - (Optional) self.highest_total: the highest dice total so far, initialized as the total of the initial dice set
        """
        self.dice_set = None  # TODO: create a new DiceSet with 5 dice of 6 sides each
        self.highest_total = None  # TODO: initialize the highest total to the initial dice sum

    def run_command(self, command):
        """
        Called after the player inputs a command. You are to implement the following commands:
        * `h` or `help` : Print a help message, showing commands the player can use.
        * (optional) `q` or `quit`: Quits the program, but prints a nice message before just before quitting.
        * `use <s> <n>` : Obtain a new set of dice. Here <n> is the number of dice, and <s> is the number of sides for each die in the set. Prints the descriptor of dice set just obtained and the dice set too.
        * `roll all`: Rolls all the dice, then prints the dice set.
        * `roll <i>`: Rolls the i-th die in the set, then prints the dice set.
        * (optional) high or highest: Prints the highest roll so far.

        Implementation Hints:
        * You can use the string `split()` method to split a string into a list of words.
        * Don't use `input()` here! The input has already been read and passed to this method.
        * Implementing `quit`? See the `exit()` function imported above.
        """
        pass

    def play(self):
        """
        Begins the game by repeatedly prompting the player for commands.
        This method has been implemented for you; you should not need to modify it.
        """
        print("Welcome to High Roller Game!")
        while True:
            player_input = input("Enter a command: ")
            self.run_command(player_input)


if __name__ == "__main__":
    HighRollerGame().play()
