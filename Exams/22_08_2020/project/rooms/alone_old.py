from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name, pension):
        budget = pension
        members_count = 1
        super().__init__(family_name, budget, members_count)
        self.room_cost = 10