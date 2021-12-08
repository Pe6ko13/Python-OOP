from project.card.trap_card import TrapCard
import unittest


class TestsTrapCard(unittest.TestCase):
    def setUp(self):
        self.card = TrapCard('Random Card')

    def test_init_should_create_correct_attributes(self):
        self.assertEqual(self.card.name, 'Random Card')
        self.assertEqual(self.card.damage_points, 120)
        self.assertEqual(self.card.health_points, 5)

    def test_name_setter_with_empty_string_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.card.name = ""
        self.assertEqual(str(cm.exception), "Card's name cannot be an empty string.")

    def test_damage_points_setter_with_negative_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.card.damage_points = -1
        self.assertEqual(str(cm.exception), "Card's damage points cannot be less than zero.")

    def test_health_points_setter_with_negative_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.card.health_points = -2
        self.assertEqual(str(cm.exception), "Card's HP cannot be less than zero.")


if __name__ == '__main__':
    unittest.main()