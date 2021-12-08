class Vet:
    animals = []       # all animals in the clinic
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []         # animals to the specific doctor

    def register_animal(self, animal_name):
        if Vet.space > len(Vet.animals):
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            self.animals.pop(self.animals.index(animal_name))
            Vet.animals.pop(Vet.animals.index(animal_name))
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic"
