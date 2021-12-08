class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if len(self.animals) < self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        # total_salaries = 0
        # for worker in self.workers:
        #     total_salaries += worker.salary
        total_salaries = sum(map(lambda worker: worker.salary, self.workers))
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_care = sum(map(lambda animal: animal.money_for_care, self.animals))
        # total_money_for_care = sum(worker.salary for worker in self.workers)
        if self.__budget >= total_money_for_care:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [repr(x) for x in self.animals if x.__class__.__name__ == 'Lion']
        result += f'----- {len(lions)} Lions:\n'
        result += '\n'.join(lions) + '\n'
        tigers = [repr(t) for t in self.animals if t.__class__.__name__ == 'Tiger']
        result += f'----- {len(tigers)} Tigers:\n'
        result += '\n'.join(tigers) + '\n'
        cheetahs = [repr(c) for c in self.animals if c.__class__.__name__ == 'Cheetah']
        result += f'----- {len(cheetahs)} Cheetahs:\n'
        result += '\n'.join(cheetahs)

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [repr(x) for x in self.workers if x.__class__.__name__ == 'Keeper']
        result += f'----- {len(keepers)} Keepers:\n'
        result += '\n'.join(keepers) + '\n'
        caretakers = [repr(t) for t in self.workers if t.__class__.__name__ == 'Caretaker']
        result += f'----- {len(caretakers)} Caretakers:\n'
        result += '\n'.join(caretakers) + '\n'
        vets = [repr(c) for c in self.workers if c.__class__.__name__ == 'Vet']
        result += f'----- {len(vets)} Vets:\n'
        result += '\n'.join(vets)

        return result





