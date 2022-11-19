import random
import unittest
from highroller import Die, DiceSet, HighRollerGame


class DieTests(unittest.TestCase):

    def test_die_init(self):
        die = Die(5, 6)
        self.assertEqual(die.sides, 6)
        self.assertEqual(die.value, 5)

    def test_die_roll(self):
        die = Die(1, 6)
        die.roll()
        self.assertTrue(1 <= die.value <= 6)

    def test_die_getters(self):
        die = Die(5, 6)
        self.assertEqual(die.get_number_sides(), 6)
        self.assertEqual(die.get_current_value(), 5)

        die = Die(1, 20)
        self.assertEqual(die.get_number_sides(), 20)
        self.assertEqual(die.get_current_value(), 1)

    def test_die_str(self):
        die = Die(5, 6)
        self.assertEqual(str(die), "[5]")
        die.roll()
        self.assertEqual(str(die), "[{}]".format(die.get_current_value()))


class DiceSetTests(unittest.TestCase):

    def test_dice_set_init(self):
        dice_set = DiceSet(6, 5)
        self.assertEqual(len(dice_set.dice), 5)
        for die in dice_set.dice:
            self.assertEqual(die.get_current_value(), 1)
            self.assertEqual(die.get_number_sides(), 6)

    def test_dice_set_descriptor(self):
        dice_set = DiceSet(6, 5)
        self.assertEqual(dice_set.get_descriptor(), "5d6")
        dice_set = DiceSet(20, 1)
        self.assertEqual(dice_set.get_descriptor(), "1d20")

    def test_dice_set_total(self):
        dice_set = DiceSet(6, 5)
        self.assertEqual(dice_set.get_total(), 5)
        dice_set.dice = [Die(i, 6) for i in range(5)]
        self.assertEqual(dice_set.get_total(), 10)

    def test_dice_set_roll_all(self):
        dice_set = DiceSet(6, 5)
        dice_set.roll_all()
        self.assertEqual(dice_set.get_total(), sum(
            [die.value for die in dice_set.dice]))

    def test_dice_set_roll_die(self):
        dice_set = DiceSet(6, 5)
        old_dice_values = [die.get_current_value() for die in dice_set.dice]
        dice_set.roll_die(0)
        for i in range(1, 5):
            self.assertEqual(
                old_dice_values[i], dice_set.dice[i].value)

    def test_dice_set_get_values(self):
        dice_set = DiceSet(6, 5)
        self.assertEqual([die.get_current_value()
                         for die in dice_set.dice], dice_set.get_current_values())

    def test_dice_set_str(self):
        dice_set = DiceSet(6, 5)
        self.assertEqual(str(dice_set), "[1][1][1][1][1]")
        dice_set.roll_all()
        self.assertEqual(str(dice_set), "[{}][{}][{}][{}][{}]".format(
            dice_set.dice[0].value,
            dice_set.dice[1].value,
            dice_set.dice[2].value,
            dice_set.dice[3].value,
            dice_set.dice[4].value,
        ))


class HighRollerGameTests(unittest.TestCase):

    def test_init(self):
        game = HighRollerGame()
        self.assertEqual(game.dice_set.get_descriptor(), "5d6")
        self.assertEqual(game.dice_set.get_total(), 5)

    def test_help(self):
        game = HighRollerGame()
        dice = list(game.dice_set.dice)
        game.run_command("help")
        self.assertEqual(dice, game.dice_set.dice)

    def test_roll_one(self):
        game = HighRollerGame()
        game.run_command("roll", ["2"])
        self.assertEqual(game.dice_set.get_total(), sum(
            [die.value for die in game.dice_set.dice]))

    def test_roll_all(self):
        game = HighRollerGame()
        game.run_command("roll", ["all"])
        self.assertEqual(game.dice_set.get_total(), sum(
            [die.value for die in game.dice_set.dice]))

    def test_use(self):
        game = HighRollerGame()
        game.run_command("use", ["20", "1"])
        self.assertEqual(len(game.dice_set.dice), 1)
        self.assertEqual(game.dice_set.get_descriptor(), "1d20")
        for die in game.dice_set.dice:
            self.assertEqual(die.get_number_sides(), 20)

    def test_unknown_command(self):
        game = HighRollerGame()
        dice = list(game.dice_set.dice)
        game.run_command("unknown")
        self.assertEqual(dice, game.dice_set.dice)


class ExtraCreditTests(unittest.TestCase):

    def test_dice_set_matches(self):
        dice_set_1 = DiceSet(6, 5)  # [1, 1, 1, 1, 1], 6 sides each
        dice_set_2 = DiceSet(6, 5)  # [1, 1, 1, 1, 1], 6 sides each
        dice_set_3 = DiceSet(5, 5)  # [1, 1, 1, 1, 1], 5 sides each
        dice_set_4 = DiceSet(6, 4)  # [1, 1, 1, 1], 6 sides each

        self.assertTrue(dice_set_1.matches(dice_set_2))
        self.assertFalse(dice_set_1.matches(dice_set_3))
        self.assertFalse(dice_set_2.matches(dice_set_4))

        dice_set_1.dice = [Die(i, 6) for i in range(1, 6)]  # [1, 2, 3, 4, 5]
        self.assertFalse(dice_set_1.matches(dice_set_2))

        dice_set_2.dice = list(
            sorted(dice_set_1.dice, key=lambda _: random.random()))
        self.assertTrue(dice_set_1.matches(dice_set_2))

    def test_quit(self):
        game = HighRollerGame()
        with self.assertRaises(SystemExit):
            game.run_command("quit")

    def test_highest(self):
        game = HighRollerGame()
        best_score = game.dice_set.get_total()

        game.run_command("highest")
        self.assertEqual(game.highest_total, best_score)

        game.run_command("roll", ["all"])
        best_score = game.dice_set.get_total()
        self.assertEqual(game.highest_total, best_score)

        game.run_command("use", ["6", "50"])
        game.run_command("roll", ["all"])
        best_score = game.dice_set.get_total()
        self.assertEqual(game.highest_total, best_score)


if __name__ == '__main__':
    unittest.main()
