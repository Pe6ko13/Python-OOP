from project.battle_field import BattleField
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
import unittest


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.battlefield = BattleField()

    def test_fight_with_attacker_dead_should_raise_error(self):
        attacker = Beginner('Peter')
        enemy = Advanced('George')
        attacker.health = 0
        with self.assertRaises(ValueError) as cm:
            self.battlefield.fight(attacker, enemy)
        self.assertEqual(str(cm.exception), "Player is dead!")

    def test_fight_with_enemy_dead_should_raise_error(self):
        attacker = Beginner('Peter')
        enemy = Advanced('George')
        enemy.health = 0
        with self.assertRaises(ValueError) as cm:
            self.battlefield.fight(attacker, enemy)
        self.assertEqual(str(cm.exception), "Player is dead!")

    def test_fight_health_increase_no_cards(self):
        enemy = Beginner('Peter')
        attacker = Advanced('George')
        self.battlefield.fight(attacker, enemy)
        self.assertEqual(enemy.health, 90)
        self.assertEqual(attacker.health, 250)

    def test_fight_health_increase_with_cards(self):
        enemy = Beginner('Peter')
        attacker = Advanced('George')
        card = MagicCard('McCard')
        attacker.card_repository.add(card)
        tcard = TrapCard('CC')
        enemy.card_repository.add(tcard)
        self.battlefield.fight(attacker, enemy)
        self.assertEqual(enemy.health, 90)
        self.assertEqual(attacker.health, 180)

    def test_dead_player_while_fighting(self):
        enemy = Beginner('Peter')
        attacker = Advanced('George')
        card = MagicCard('McCard')
        tcard = TrapCard('CC')
        attacker.card_repository.add(tcard)
        tcard = TrapCard('CC1')
        attacker.card_repository.add(tcard)
        tcard = TrapCard('CC2')
        attacker.card_repository.add(tcard)
        enemy.card_repository.add(card)
        with self.assertRaises(ValueError) as ex:
            self.battlefield.fight(attacker, enemy)
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")
        self.battlefield.fight(attacker, enemy)


if __name__ == '__main__':
    unittest.main()
