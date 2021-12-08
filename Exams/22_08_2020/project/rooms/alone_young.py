from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, name, salary):
        budget = salary
        members_count = 1
        super().__init__(name, budget, members_count)
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)
