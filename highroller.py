"""
Name:
Date:
Description:
"""

from random import randint

"""
####### Die Class: ######
A simple class for representing die objects. A die has a given number of
sides (at least) four, set when the die is constructed and which can never
be changed. The die's value can be changed, but only by calling its roll()
method.
"""


class Die():

    """
    Constructs a die with the given starting value and number of sides.
    """

    def __init__(self, initial_value, sides):
        self.value = initial_value
        self.sides = sides

    """
    Simulates a roll by randomly updating the value of this die. 
    In addition to mutating the die's value, this method also 
    returns the new updated value.
    """

    def roll(self):
        self.value = randint(1, self.sides)

    # Returns the number of sides of this die.
    def get_number_sides(self):
        return self.sides

    # Returns the current value of this die.
    def get_current_value(self):
        return self.value

    """
    Returns a string representation of this die, which is its value enclosed in square
    brackets, without spaces, for example "[5]".
    """

    def __str__(self):
        return "[{}]".format(self.value)


"""
####### DiceSet Class: ######
A dice set holds a collection of Die objects. All of the die objects have
the same number of sides. 
"""


class DiceSet():

    """
    Creates a DiceSet containing the given number of dice, each with the 
    given number of sides. All die values start off as 1.
    """

    def __init__(self, sides_each_die, number_of_dice):
        self.dice = [Die(1, sides_each_die) for _ in range(number_of_dice)]

    """
    Returns the descriptor of the dice set; for example "5d20" for a set with
    five dice of 20 sides each; or "2d6" for a set of two six-sided dice.
    """

    def get_descriptor(self):
        return str(len(self.dice)) + "d" + str(self.dice[0].get_number_sides())

    # Returns the total of the values of each die in the set.
    def get_total(self):
        return sum([die.get_current_value() for die in self.dice])

    # Rolls all the dice in the set.
    def roll_all(self):
        for die in self.dice:
            die.roll()

    # Rolls the i-th die, updating its value.
    def roll_die(self, i):
        self.dice[i].roll()

    # Returns the values of each of the dice in a list.
    def get_current_values(self):
        return [die.get_current_value() for die in self.dice]

    """
    Returns whether this dice set has the same distribution of values as
    another dice set. The two dice sets must have the same number of dice
    and the same number of sides per dice, and there must be the same
    number of each value in each set.
    """

    def matches(self, dice_set):
        return self.get_descriptor() == dice_set.get_descriptor() and sorted(self.get_current_values()) == sorted(dice_set.get_current_values())

    """
    Returns a string representation in which each of the die strings are
    joined without a separator, for example: "[2][5][2][3]".
    """

    def __str__(self):
        return "".join([str(die) for die in self.dice])


def main():
    """ 
    ####### Main Program: ######
    The program should begin by printing a welcome message. 
    Then it repeatedly asks the user to enter a command and carries
    it out. Each command will either print a response or an error 
    message, followed by a blank line.
    """
    print("Welcome to HighRollerGame!")

    dice = DiceSet(6, 5)
    highest = dice.get_total()
    print(dice)

    while True:
        player_input = input("Enter a command: ")
        if player_input == "":
            player_input = "help"
        command, *args = player_input.split()
        if command == "roll":
            if args[0] == "all":
                dice.roll_all()
            else:
                dice.roll_die(int(args[0]))
            print(dice)
            highest = max(highest, dice.get_total())
        elif command == "use":
            dice = DiceSet(int(args[0]), int(args[1]))
            highest = max(highest, dice.get_total())
            print(dice.get_descriptor())
            print(dice)
        elif command == "highest" or command == "high":
            print(highest)
        elif command == "h" or command == "help":
            print("Commands: roll all, roll i, h, help, q, quit")
        elif command == "q" or command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command, use h or help for help!")


if __name__ == "__main__":
    main()
