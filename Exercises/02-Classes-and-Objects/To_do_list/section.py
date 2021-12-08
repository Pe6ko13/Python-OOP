from CL_and_OBJ.To_do_list.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self. name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        filtered_tasks = [t for t in self.tasks if t.name == task_name]
        if filtered_tasks:
            task = filtered_tasks[0]
            task.completed = True
            return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        all_not_completed = [t for t in self.tasks if not t.completed]
        removed_task = len(self.tasks) - len(all_not_completed)
        self.tasks = all_not_completed
        return f"Cleared {removed_task} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for t in self.tasks:
            result += t.details() + '\n'
        return result

    # completed_tasks=0
    # def complete_task(self, task_name: str):
    #     if task_name not in [t.name for t in self.tasks]:
    #         return f"Could not find task with the name {task_name}"
    #     task = [t for t in self.tasks if t.name == task_name][0]
    #     task.completed = True
    #     self.completed_tasks += 1
    #     return f"Completed task {task_name}"
    #
    # def clean_section(self):
    #     to_remove = []
    #     for t in self.tasks:
    #         if t.completed:
    #             to_remove.append(t)
    #     self.tasks = [item for item in self.tasks if item not in to_remove]
    #     return f"Cleared {self.completed_tasks} tasks."


