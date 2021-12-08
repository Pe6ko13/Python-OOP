from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.cards = []

    def add(self, card: Card):
        if any(c.name == card.name for c in self.cards):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        find_card = [c for c in self.cards if card == c.name][0]
        self.cards.remove(find_card)

    def find(self, name: str):
        find_card = [c for c in self.cards if name == c.name][0]
        return find_card

    @property
    def count(self):
        return len(self.cards)
