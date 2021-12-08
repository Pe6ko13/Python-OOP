from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        # self.count = 0
        self.players = []

    @property
    def count(self):
        return len(self.players)

    def add(self, player: Player):
        # names = [p.username for p in self.players]
        # if player.username in names:
        #     raise ValueError(f"Player {player.username} already exists!")
        if any(p.username == player.username for p in self.players):
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        # self.count += 1

    def remove(self, player_name):
        if player_name == '':
            raise ValueError("Player cannot be an empty string!")
        find_pl = [p for p in self.players if player_name == p.username][0]
        self.players.remove(find_pl)
        # self.count -= 1

    def find(self, useranme):
        find_pl = [p for p in self.players if useranme == p.username][0]
        return find_pl
