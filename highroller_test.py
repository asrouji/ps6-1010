import unittest
from highroller import Die, DiceSet


class DieTests(unittest.TestCase):

    def test_die_init(self):
        die = Die(5, 6)
        self.assertEqual(die.sides, 6)
        self.assertEqual(die.value, 5)

    def test_die_roll(self):
        die = Die(1, 6)
        die.roll()
        self.assertTrue(1 <= die.get_current_value() <= 6)

    def test_die_getters(self):
        die = Die(5, 6)
        self.assertEqual(die.get_number_sides(), 6)
        self.assertEqual(die.get_current_value(), 5)

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
        self.assertTrue(5 <= dice_set.get_total() <= 30)

    def test_dice_set_roll_die(self):
        dice_set = DiceSet(6, 5)
        dice_values = [die.get_current_value() for die in dice_set.dice]
        dice_set.roll_die(0)
        for i in range(1, 5):
            self.assertEqual(
                dice_values[i], dice_set.dice[i].get_current_value())

    def test_dice_set_get_values(self):
        dice_set = DiceSet(6, 5)
        self.assertEqual([die.get_current_value()
                         for die in dice_set.dice], dice_set.get_current_values())

    def test_dice_set_str(self):
        dice_set = DiceSet(6, 5)
        self.assertEqual(str(dice_set), "[1][1][1][1][1]")
        dice_set.roll_all()
        self.assertEqual(str(dice_set), "[{}][{}][{}][{}][{}]".format(
            dice_set.dice[0].get_current_value(),
            dice_set.dice[1].get_current_value(),
            dice_set.dice[2].get_current_value(),
            dice_set.dice[3].get_current_value(),
            dice_set.dice[4].get_current_value(),
        ))


class ExtraCreditTests(unittest.TestCase):
    def test_dice_set_matches(self):
        dice_set_1 = DiceSet(6, 5)
        dice_set_2 = DiceSet(6, 5)
        self.assertTrue(dice_set_1.matches(dice_set_2))
        dice_set_1.dice = [Die(i, 6) for i in range(1, 6)]
        self.assertFalse(dice_set_1.matches(dice_set_2))
        dice_set_2.dice = [Die(5 - i, 6) for i in range(5)]
        self.assertTrue(dice_set_1.matches(dice_set_2))


if __name__ == '__main__':
    unittest.main()
