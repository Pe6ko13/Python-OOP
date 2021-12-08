from project.card.card_repository import CardRepository
import unittest
from project.player.magiccard import MagicCard


class TestPlayerRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.cr = CardRepository()

    def test_set_attr(self):
        self.assertEqual(self.cr.count, 0)
        self.assertEqual(len(self.cr.cards), 0)

    def test_add_raises(self):
        c = MagicCard('Jok')
        self.cr.add(c)
        with self.assertRaises(ValueError) as ex:
            self.cr.add(c)
        self.assertEqual("Card Jok already exists!", str(ex.exception))

    def test_add(self):
        c = MagicCard('Jok')
        self.cr.add(c)
        self.assertEqual(self.cr.count, 1)

    def test_remove_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cr.remove('')
        self.assertEqual("Card cannot be an empty string!", str(ex.exception))

    def test_remove_card(self):
        c = MagicCard('Jok')
        self.cr.add(c)
        self.assertEqual(self.cr.count, 1)
        self.cr.remove('Jok')
        self.assertEqual(self.cr.count, 0)

    def test_find_card(self):
        c = MagicCard('Jok')
        self.cr.add(c)
        res = self.cr.find('Jok')
        self.assertEqual(res.name, 'Jok')


if __name__ == '__main__':
    unittest.main()