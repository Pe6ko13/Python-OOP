class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        # total_consumption = sum((room.expenses + room.room_cos)t for room in self.rooms)
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        s = []
        rooms_to_remove = []
        for room in self.rooms:
            monthly_expenses = room.expenses * 30 + room.room_cost * 30
            if room.budget >= monthly_expenses:
                room.budget -= monthly_expenses
                s.append(f"{room.family_name} paid {monthly_expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                 s.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                 self.rooms.remove(room)
        # for room in rooms_to_remove:
        #     self.rooms.pop(self.rooms.index(room))
        return '\n'.join(s)

    def status(self):
        s = ''
        all_people_in_the_hotel = sum([room.members.count for room in self.rooms])
        s += f'Total population: {all_people_in_the_hotel}'
        for room in self.rooms:
            s += f'{room.family_name} with {room.members_count} members.Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$'
            for idx, child in enumerate(room.children, 1):
                cost_for_one_month = child.cost * 30
                s += f'--- Child {idx} monthly cost: {cost_for_one_month:.2f}$\n'
            cost_of_all_appliances_for_one_month = sum([a.get_monthly_expenses() for a in room.appliances])
            s += f'--- Appliances monthly cost: {cost_of_all_appliances_for_one_month:.2f}$\n'
        return s
