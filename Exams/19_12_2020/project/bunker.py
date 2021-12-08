class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @staticmethod
    def filter_or_raise(list_to_filter, type_name, exc_message):
        res = [el for el in list_to_filter if el.__class__.__name__ == type_name]
        if not res:
            raise IndexError(exc_message)
        return res

    @property
    def food(self):
        return Bunker.filter_or_raise(self.supplies, "FoodSupply", "There are no food supplies left!")

    @property
    def water(self):
        water_sup = [x for x in self.supplies if x.__class__.__name__ == 'WaterSupply']
        if len(water_sup) == 0:
            raise IndexError("There are no water supplies left!")
        return water_sup
    
    @property
    def painkillers(self):
        painkiller_sup = [x for x in self.medicine if x.__class__.__name__ == 'Painkiller']
        if not painkiller_sup:
            raise IndexError("There are no painkillers left!")
        return painkiller_sup
    
    @property
    def salves(self):
        salves_sup = [x for x in self.medicine if x.__class__.__name__ == 'Salve']
        if not salves_sup:
            raise IndexError("There are no salves left!")
        return salves_sup

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            pill = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
            # if medicine_type == 'Painkiller':
            #     pill = self.painkillers.pop()
            # else:
            #     pill = self.salves.pop()
            self.medicine.remove(pill)
            pill.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            if sustenance_type == 'FoodSupply':
                sup = self.food.pop()
            else:
                sup = self.water.pop()
            survivor.needs += sup.needs_increase
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for sur in self.survivors:
            sur.needs -= sur.age * 2
            self.sustain(sur, "FoodSupply")
            self.sustain(sur, "WaterSupply")

