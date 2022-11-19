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
        self.value = initial_value
        self.sides = sides

    def roll(self):
        """
        Simulates a roll by randomly updating the value of this die. 
        In addition to mutating the die's value, this method also 
        returns the new updated value.
        """
        self.value = randint(1, self.sides)

    def get_number_sides(self):
        """
        Returns the number of sides of this die.
        """
        return self.sides

    def get_current_value(self):
        """
        Returns the current value of this die.
        """
        return self.value

    def __str__(self):
        """
        Returns a string representation of this die, which is its value enclosed in square
        brackets, without spaces, for example "[5]".
        """
        return "[{}]".format(self.value)


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
        self.dice = [Die(1, sides_each_die) for _ in range(number_of_dice)]

    def get_descriptor(self):
        """
        Returns the descriptor of the dice set; for example "5d20" for a set with
        five dice of 20 sides each; or "2d6" for a set of two six-sided dice.
        """
        return str(len(self.dice)) + "d" + str(self.dice[0].get_number_sides())

    # Returns the total of the values of each die in the set.
    def get_total(self):
        """
        Returns the total of the values of each die in the set.
        """
        return sum([die.get_current_value() for die in self.dice])

    def roll_all(self):
        """
        Rolls all of the dice in the set.
        """
        [die.roll() for die in self.dice]

    def roll_die(self, i):
        """
        Rolls the die at the given index in the set.
        """
        self.dice[i].roll()

    def get_current_values(self):
        """
        Returns a list of the current values of each die in the set.
        """
        return [die.get_current_value() for die in self.dice]

    def matches(self, dice_set):
        """
        Returns whether this dice set has the same distribution of values as
        another dice set. The two dice sets must have the same number of dice
        and the same number of sides per dice, and there must be the same
        number of each value in each set.
        """
        return self.get_descriptor() == dice_set.get_descriptor() and sorted(self.get_current_values()) == sorted(dice_set.get_current_values())

    def __str__(self):
        """
        Returns a string representation in which each of the die strings are
        joined without a separator, for example: "[2][5][2][3]".
        """
        return "".join([str(die) for die in self.dice])


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
        self.dice_set = DiceSet(6, 5)
        self.highest_total = self.dice_set.get_total()

    def run_command(self, command, args=[]):
        """
        Called after the player enters a command. This method accepts two arguments:
        - command: the first word of the given command (e.g. "roll", "use", "help", etc.)
        - args: list of command arguments (e.g. ["5", "4"] for "use 5 4" or ["all"] for "roll all")
        """
        match command:
            case "roll":
                if args[0] == "all":
                    self.dice_set.roll_all()
                else:
                    self.dice_set.roll_die(int(args[0]))
                print(self.dice_set)
            case "use":
                self.dice_set = DiceSet(int(args[0]), int(args[1]))
                print(self.dice_set.get_descriptor())
                print(self.dice_set)
            case "highest":
                print(f'Highest score so far: {self.highest_total}')
            case "help":
                print(
                    "Commands: roll all, roll <die>, use <sides> <count>, highest, help, quit")
            case "quit":
                print("Goodbye!")
                exit()
            case _:
                print("Unknown command")
        if self.dice_set.get_total() > self.highest_total:
            self.highest_total = self.dice_set.get_total()

    def play(self):
        """
        Begins the game by repeatedly prompting the player for commands.
        This method has been implemented for you; you should not need to modify it.
        """
        print("Welcome to High Roller Game!")
        while True:
            command, *args = input("Enter a command: ").split()
            self.run_command(command, args)


if __name__ == "__main__":
    HighRollerGame().play()
