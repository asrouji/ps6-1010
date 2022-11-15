**CMSI 1010** Computer Programming & Laboratory, Fall 2022

# Problem Set 6
**Due 11:59pm PT 11/08**

## (Optional) Reading
As before, the reading is from the [_Think Python_ textbook](http://greenteapress.com/thinkpython2/thinkpython2.pdf):
* Chapter 18

Take notes from these readings and submit them as part of this pset. If you opt to do this, you may submit them as a separate file `ps6_notes.txt`/`ps6_notes.md` or you may add them directly to this README file. (files that end in `.md` look best when written in [GitHub Markdown](https://guides.github.com/features/mastering-markdown/))

## Programming

0. **Understanding Inheritance**
    This is a paper and pencil exercise—please edit this file at the indicated locations with your answers.

    Consider the following code:

    ```python
    class Spell(object):
        def __init__(self, incantation, name):
            self.name = name
            self.incantation = incantation

        def __str__(self):
            return self.name + ' ' + self.incantation + '\n' + self.get_description()

        def get_description(self):
            return 'No description'

        def execute(self):
            print(self.incantation)

    class Accio(Spell):
        def __init__(self):
            Spell.__init__(self, 'Accio', 'Summoning Charm')

    class Confundo(Spell):
        def __init__(self):
            Spell.__init__(self, 'Confundo', 'Confundus Charm')

        def get_description(self):
            return 'Causes the victim to become confused and befuddled.'

    def study_spell(spell):
        print(spell)

    spell = Accio()
    spell.execute()
    study_spell(spell)
    study_spell(Confundo())
    ```

    1. What are the parent and child classes here?

        ```
        Replace this section with your answer. For best results, preserve the
        indentation and stay between the ``` delimiters.
        ```

    2. What does the code print out? (Try figuring it out without running it in Python.) Please mention which lines of code are printing which lines of output.

        ```
        Replace this section with your answer. For best results, preserve the
        indentation and stay between the ``` delimiters.
        ```

    3. Which `get_description` method is called when `study_spell(Confundo())` is executed? Why?

        ```
        Replace this section with your answer. For best results, preserve the
        indentation and stay between the ``` delimiters.
        ```

    4. What do we need to do so that `print Accio()` will print the appropriate description (`This charm summons an object to the caster, potentially over a significant distance`)?  Write down the code that we need to add and/or change.

        ```
        Replace this section with your answer. For best results, preserve the
        indentation and stay between the ``` delimiters.
        ```

1. **High Roller** - `highroller.py`

    You’ve become really good at video games but have started wondering what games were like before Pong. Did people play games on the... command line? What was it like to play a game just with text? You decide to try writing such a game in Python, complete with old-fashioned text menus containing numbered options. And what a great idea this is! 

    
    1. **Complete the Die class:** Take a look at the `Die` class and complete it. This class represents a single die, with an immutable number of sides (at least 4) and a mutable current value (between 1 and the number of sides). Implement the following methods:
     ```
      __init__()            // Constructor for a die with the given number of sides
      roll()                // Returns a value as a result of randomly rolling this die
      get_current_value()     // Returns the current value of this die which resulted from the last rol
      get_number_sides()   // Gets the number of sides
      __str__ ()       // Returns a String representation of the value of this die, e.g., “[11]”
   ```
    
    ![](dice.png)
    
    2. **Complete the DiceSet class:** Next, make a class called DiceSet, a collection of at least two Die objects, all with the same number
of sides. You are not allowed to add or remove die objects from a DiceSet once constructed. But you are allowed to roll the dice in the set. Complete the following methods:
```
    __init__()          // Constructor
    get_total()          // Returns the current total of this set of dice
    get_descriptor()     // "5d20” for a set with 5 dice of 20 sides each
    roll_all()           // Randomly rolls all of the dice in this set
    roll_die()           // Randomly rolls the die at index i
    get_current_values()  // Returns the values of all the dice as a List of integers
    matches()           // (optional) `true` if both dice sets are effectively the same: same number of dice, same die size, and same current values—in any order
    __str__()           // Returns a String representation of this set of dice, e.g., “[3][9][12][4]”
```
    
   3. **Completing the Game:** This is to be a console-/terminal-based application run from the command line. The program should begin by printing a welcome message. Then it repeatedly asks the user to enter a command and carries it out. Each command will either print a response or an error message, followed by a blank line. If the command is q, the program will cleanly exit. The commands to support are:
 ```   
    * h or help : Print a help message, showing all the commands and what they do.
    * q or quit: Quits the program, but prints a nice message before just before quitting. (This part is optional)
    * use <s> <n> : Obtain a new set of dice. Here <n> is the number of dice, which must be between 2 and 99; and <s> is the number of sides for each die in the set, which must be between 4 and 99. Prints the descriptor of dice set just obtained and the dice set too.
    * roll all: Rolls all the dice, then prints the dice set.
    * roll <i>: Rolls the i-th die in the set, then prints the dice set.
    * high or highest: Prints the highest roll so far. (This part is optional)
```  
  Note that not every method from the Die and DiceSet class is necessarily used in this game. That’s perfectly fine. When you write classes like Die and DiceSet, you want them to be used widely by many people, not just by you. Imagine that you can use these same classes for a role-playing game, for instance, or perhaps traditional dice games like craps (uhhh, when you’re old enough to play that). 
  
  Notice from the output above, and make sure to implement in your solution, tso that any command that is not understood displays “I don’t understand”.


## What to turn in
1. Submit the electronic copy of any files that you created/modified on your clone. In the Terminal (within your repository clone folder), type these commands. Note that you may repeat these add-commit-push sequences as frequently as you like, based on your progress:
    ```bash
    git add README.md            # For written/image answers to questions.
    git add ps6_notes.md         # If submitting reading notes as a separate file.
    git add highroller.py
    git commit -m "adding files for ps6" # Ideally, personalize this!
    git push
    # By all means, feel free to add/commit/push multiple times before the due date.
    ```

2. Edit this _README.md_ file to include your answers to the following questions:
    * **Number of hours spent** working on this pset:
    * (Optional) Feel free to let us know what you liked/disliked about this pset, what you learned, etc:

## Points breakdown
| Category | Points |
| -------- | -----: |
| Notes (optional) | 3 points extra credit |
| Written answers | 7.5 points each, 30 points total |
| `highroller.py` | 70 points |
| match (optional) | 5 points extra credit |
| track high score (optional) | 5 points extra credit |
| quit (optional)| 5 points extra credit |
| **Total** | 100 points |
