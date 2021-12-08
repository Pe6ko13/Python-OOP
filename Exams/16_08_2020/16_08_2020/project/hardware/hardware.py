from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.used_memory = 0
        self.used_capacity = 0


    def install(self, software: Software):
        if self.capacity - self.used_capacity >= software.capacity_consumption and \
                self.memory - self.used_memory >= software.memory_consumption:
            self.software_components.append(software)
            self.used_memory += software.memory_consumption
            self.used_capacity += software.capacity_consumption
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)
