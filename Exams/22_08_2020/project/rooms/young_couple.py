from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, name, salary_one, salary_two):
        budget = salary_one + salary_two
        members_count = 2
        super().__init__(name, budget, members_count)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * members_count
        self.calculate_expenses(self.appliances)