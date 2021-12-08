import unittest

from project.player.magiccard import MagicCard
from project.player.player_repository import PlayerRepository

from player.player import Player


class TestPlayerRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.pl = PlayerRepository()

    def test_set_attr(self):
        self.assertEqual(self.pl.count, 0)
        self.assertEqual(len(self.pl.players), 0)

    def test_add_raises(self):
        p = Player('Pesho')
        self.pl.add(p)
        with self.assertRaises(ValueError) as ex:
            self.pl.add(p)
        self.assertEqual("Player Pesho already exists!", str(ex.exception))

    def test_add(self):
        p = MagicCard('Pesho')
        self.pl.add(p)
        self.assertEqual(self.pl.count, 1)

    def test_remove_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pl.remove('')
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))

    def test_remove_player(self):
        p = MagicCard('Pesho')
        self.pl.add(p)
        self.assertEqual(self.pl.count, 1)
        self.pl.remove('Pesho')
        self.assertEqual(self.pl.count, 0)

    def test_find_player(self):
        p = MagicCard('Pesho')
        self.pl.add(p)
        res = self.pl.find('Pesho')
        self.assertEqual(res.username, 'Pesho')


if __name__ == '__main__':
    unittest.main()