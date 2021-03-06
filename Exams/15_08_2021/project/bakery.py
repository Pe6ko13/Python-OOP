from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        foo = [f for f in self.food_menu if f.name == name]
        if not foo:
            if food_type == "Bread":
                f = Bread(name, price)
                self.food_menu.append(f)
                return f"Added {f.name} ({food_type}) to the drink menu"
            elif food_type == "Cake":
                f = Cake(name, price)
                self.drinks_menu.append(f)
                return f"Added {name} ({food_type}) to the drink menu"
        else:
            raise Exception(f"{food_type} {name} is already in the menu!")

    def add_drink(self, drink_type: str, name: str, portion: int, brand:str):
        if name not in self.drinks_menu:
            drink = ""
            if drink_type == "Tea":
                drink = Tea(name, portion, brand)
                self.drinks_menu.append(drink)
            elif drink_type == "Water":
                drink = Water(name, portion, brand)
                self.drinks_menu.append(drink)
            return f"Added {drink.name} ({drink.brand}) to the drink menu"
        else:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        # dr = [d for d in self.drinks_menu if d.name == name][0]
        # if dr in self.food_menu:
        #     raise Exception(f"{drink_type} {dr.name} is already in the menu!")
        # if drink_type == "Tea":
        #     drink = Tea(name, portion, brand)
        #     self.drinks_menu.append(drink)
        #     return f"Added {drink.name} ({drink.brand}) to the drink menu"
        # elif drink_type == "Water":
        #     drink = Water(name, portion, brand)
        #     self.drinks_menu.append(drink)
        #     return f"Added {drink.name} ({drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        searched_table = [t for t in self.tables_repository if t.table_number == table_number]
        if searched_table:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == "OutsideTable":
            self.tables_repository.append(OutsideTable(table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for t in self.tables_repository:
            if not t.is_reserved and t.capacity >= number_of_people:
                # t.reserve(number_of_people)
                return f"Table {t.number} has been reserved for {number_of_people} people"
            else:
                return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        else:

            table = table[0]
            food_not_in_menu = []
            for food_name in args:
                is_found = False
                for food in self.food_menu:
                    if food.name == food_name:
                        table.order_food(food)
                        is_found = True
                        break
                if not is_found:
                    food_not_in_menu.append(food_name)

            result = f"Table {table.table_number} ordered:\n"
            for food in table.food_orders:
                result += f"{repr(food)}\n"
            if food_not_in_menu:
                result += f"{self.name} does not have in the menu:\n"
                for food in food_not_in_menu:
                    result += f"{food}\n"

            return result

    def order_drink(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            drinks_not_in_menu = []
            for drink_name in args:
                is_found = False
                for drink in self.drinks_menu:
                    if drink.name == drink_name:
                        table.order_drink(drink)
                        is_found = True
                        break
                if not is_found:
                    drinks_not_in_menu.append(drink_name)

            result = f"Table {table.table_number} ordered:\n"
            for drink in table.drink_orders:
                result += f"{repr(drink)}\n"
            if drinks_not_in_menu:
                result += f"{self.name} does not have in the menu:\n"
                for drink in drinks_not_in_menu:
                    result += f"{drink}\n"

            return result

        return f"Could not find table {table_number}"

    def leave_table(self, table_number: int):
        table = [t for t in self.tables_repository if t.number == table_number][0]
        if table:
            table_bill = table.get_bill()
            table.clear()
            # self.total_income += table_bill
            return f"Table: {table.table_number}\n"\
                   f"Bill: {table_bill:.2f}"

    def get_free_tables_info(self):
        info = []
        for t in self.tables_repository:
            # if not t.is_reserved:
            info.append(t.free_table_info())
        return '\n'.join(info)

    def get_total_income(self):
        # for f in self.food_menu:
        #     self.total_income += f.price
        # for d in self.drinks_menu:
        #     self.total_income += d.price
        return f"Total income: {self.total_income:.2f}lv"
