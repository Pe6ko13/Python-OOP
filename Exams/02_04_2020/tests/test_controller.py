import unittest
from project.controller import Controller

REPRESENTATION = 'Username: Pesho - Health: 50 - Cards 1\n'\
    '### Card: Jok - Damage: 5'


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        self.cont = Controller()

    def test_add_player(self):
        self.assertEqual(self.cont.player_repository.count, 0)
        res = self.cont.add_player('Beginner', 'Pesho')
        self.assertEqual(self.cont.player_repository.count, 1)
        self.assertEqual("Successfully added player of type Beginner with username: Pesho", res)

    def test_add_card(self):
        self.assertEqual(self.cont.card_repository.count, 0)
        res = self.cont.add_card('Magic', 'Jok')
        self.assertEqual(self.cont.card_repository.count, 1)
        self.assertEqual("Successfully added card of type MagicCard with name: Jok", res)

    def test_add_player_card(self):
        self.assertEqual(self.cont.player_repository.count, 0)
        self.assertEqual(self.cont.card_repository.count, 0)
        self.cont.add_player('Beginner', 'Pesho')
        self.cont.add_card('Magic', 'Jok')
        self.assertEqual(self.cont.player_repository.count, 1)
        self.assertEqual(self.cont.card_repository.count, 1)
        res = self.cont.add_player_card('Pesho', 'Jok')
        self.assertEqual(res, "Successfully added card: Jok to user: Pesho")

    def test_fight(self):
        self.cont.add_player('Beginner', 'Pesho')
        self.cont.add_player('Advanced', 'Gosho')
        res = self.cont.fight('Pesho', 'Gosho')
        self.assertEqual(res, "Attack user health 250 - Enemy user health 90")

    def test_report(self):
        self.cont.add_player('Beginner', 'Pesho')
        self.cont.add_card('Magic', 'Jok')
        self.cont.add_player_card('Pesho', 'Jok')
        res = self.cont.report()
        self.assertEqual(res, REPRESENTATION)






