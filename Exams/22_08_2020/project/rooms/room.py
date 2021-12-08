from EXAM_PREP.POE_22_08_2020.project.appliances.appliance import Appliance
from EXAM_PREP.POE_22_08_2020.project.people.child import Child


class Room:
    family_name: str
    budget: float
    members_count: int
    children: list = []
    appliances = []

    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses
    
    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total = 0
        # self.expenses = sum(el.cost*30 for arg in args for el in arg)
        # for arg in args:
        #     for i in arg:
        #         if isinstance(i, Appliance):
        #             total += i.get_monthly_expense()
        #         elif isinstance(i, Child):
        #             total += i.cost * 30
        for arg in args:
            for element in arg:
                total += element.cost * 30
        self.expenses = total
