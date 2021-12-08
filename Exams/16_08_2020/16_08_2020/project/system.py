from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        find_hard = [h for h in System._hardware if h.name == hardware_name]
        if not find_hard:
            return "Hardware does not exist"
        hard = find_hard[0]
        soft = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hard.install(soft)
            System._software.append(soft)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption:  int):
        find_hard = [h for h in System._hardware if h.name == hardware_name]
        if not find_hard:
            return "Hardware does not exist"
        hard = find_hard[0]
        soft = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hard.install(soft)
            System._software.append(soft)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        hard = [h for h in System._hardware if h.name == hardware_name]
        soft = [s for s in System._software if s.name == software_name]
        if hard and soft:
            hard = hard[0]
            soft = soft[0]
            hard.uninstall(soft)
            System._software.remove(soft)
        return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        return f'System Analysis\n' \
                f'Hardware Components: {len(System._hardware)}\n' \
                f'Software Components: {len(System._software)}\n' \
                f'Total Operational Memory: {sum([h.used_memory for h in System._hardware])} / {sum(h.memory for h in System._hardware)}\n' \
                f'Total Capacity Taken: {sum([h.used_capacity for h in System._hardware])} / {sum([h.capacity for h in System._hardware])}'

    @staticmethod
    def system_split():
        res = ''
        for h in System._hardware:
            res += f"Hardware Component - {h.name}\n"
            res += f"Express Software Components: {len([s for s in h.software_components if isinstance(s, ExpressSoftware)])}\n"
            res += f"Light Software Components: {len([s for s in h.software_components if isinstance(s, LightSoftware)])}\n"
            res += f"Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.memory}\n"
            res += f"Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.capacity}\n"
            res += f"Type: {h.type}\n"
            res += f"Software Components: {'None' if not [s.name for s in h.software_components] else ', '.join([s.name for s in h.software_components])}"
        return res


System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
print(System.register_express_software("HDD", "Test2", 100, 100))
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())
