from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, name, pension_one, pension_two):
        budget = pension_one + pension_two
        members_count = 2
        super().__init__(name, budget, members_count)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * members_count
        self.calculate_expenses(self.appliances)
