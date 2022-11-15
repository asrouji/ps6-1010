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
  
    # Constructs a die with the given starting value and number of sides.
    def __init__(self, initial_value, sides):
      pass

    """
    Simulates a roll by randomly updating the value of this die. 
    In addition to mutating the die's value, this method also 
    returns the new updated value.
    """
    def roll(self):       
      pass
    
    # Returns the number of sides of this die.
    def get_number_sides(self):
      pass

    # Returns the current value of this die.
    def get_current_value(self):
      pass

    """
    Returns a string representation of this die, which is its value enclosed in square
    brackets, without spaces, for example "[5]".
    """
    def __str__(self):
      pass

     
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
      pass

    """
    Returns the descriptor of the dice set; for example "5d20" for a set with
    five dice of 20 sides each; or "2d6" for a set of two six-sided dice.
    """ 
    def get_descriptor(self):
      pass
    
    # Returns the total of the values of each die in the set.
    def get_total(self):
      pass
     
    # Rolls all the dice in the set.
    def roll_all(self):
      pass
    
    # Rolls the i-th die, updating its value.
    def roll_die(self, i):
      pass
    
    # Returns the values of each of the dice in a list.
    def get_current_values(self):
      pass
     
    """
    Returns whether this dice set has the same distribution of values as
    another dice set. The two dice sets must have the same number of dice
    and the same number of sides per dice, and there must be the same
    number of each value in each set.
    """
    def matches(self, dice_set):
     pass
    
    """
    Returns a string representation in which each of the die strings are
    joined without a separator, for example: "[2][5][2][3]".
    """
    def __str__(self):
     pass
    
    
    
 
""" 
####### Main Program: ######
The program should begin by printing a welcome message. 
Then it repeatedly asks the user to enter a command and carries
it out. Each command will either print a response or an error 
message, followed by a blank line.
"""

 
