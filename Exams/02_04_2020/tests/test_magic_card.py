from project.card.magic_card import MagicCard
import unittest


class TestsMagicCard(unittest.TestCase):
    def setUp(self):
        self.card = MagicCard('Random Card')

    def test_init_should_create_correct_attributes(self):
        self.assertEqual(self.card.name, 'Random Card')
        self.assertEqual(self.card.damage_points, 5)
        self.assertEqual(self.card.health_points, 80)

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
            self.card.health_points = -1
        self.assertEqual(str(cm.exception), "Card's HP cannot be less than zero.")


if __name__ == '__main__':
    unittest.main()