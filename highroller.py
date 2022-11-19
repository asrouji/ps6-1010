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
        return self.value

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

    def get_total(self):
        """
        Returns the total of the values of each die in the set.
        """
        return sum(self.get_current_values())

    def roll_all(self):
        """
        Rolls all of the dice in the set, and returns the total of the new values.
        """
        for die in self.dice:
            die.roll()
        return self.get_total()

    def roll_die(self, i):
        """
        Rolls the die at the given index in the set, and returns the new value.
        """
        return self.dice[i].roll()

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
        match command.split():
            case ["h" | "help"]:
                print(
                    "Commands: h or help, q or quit, use <s> <n>, roll all, roll <i>, high or highest")
            case ["q" | "quit"]:
                print("Thanks for playing!")
                exit(0)
            case ["use", sides_each_die, number_of_dice]:
                self.dice_set = DiceSet(
                    int(sides_each_die), int(number_of_dice))
                print(self.dice_set.get_descriptor())
                print(self.dice_set)
            case ["roll", "all"]:
                print(self.dice_set.roll_all())
                print(self.dice_set)
            case ["roll", index]:
                self.dice_set.roll_die(int(index))
                print(self.dice_set)
            case ["high" | "highest"]:
                print(self.highest_total)
            case _:
                print("Invalid command")
        if self.dice_set.get_total() > self.highest_total:
            self.highest_total = self.dice_set.get_total()

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
