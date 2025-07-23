import json
import os
from task import Task, Status
from tabulate import tabulate

class ToDoList:
    def __init__(self, filename="tasks.json", id_file="id_counter.txt"):
        self.tasks = {}  # key = task_id, value = Task object
        self.filename = filename
        self.id_file = id_file
        self.next_id = self.load_last_id()
        self.load_tasks()

    def load_last_id(self):
        if not os.path.exists(self.id_file):
            with open(self.id_file, "w") as f:
                f.write("1")
            return 1
        with open(self.id_file, "r") as f:
            return int(f.read())

    def save_last_id(self):
        with open(self.id_file, "w") as f:
            f.write(str(self.next_id))

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks[task.id] = task
        self.next_id += 1
        self.save_tasks()
        self.save_last_id()

    def update_task_status(self, task_id, new_status):
        task = self.tasks.get(task_id)
        if task:
            task.update_status(Status(new_status))
            self.save_tasks()
            return True
        return False

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            self.save_tasks()
            return True
        return False

    def filter_by_status(self, status_str):
        status = Status(status_str)
        return [task for task in self.tasks.values() if task.status == status]

    def list_tasks(self):
        return list(self.tasks.values())

    def save_tasks(self):
        data = {str(task_id): task.to_dict() for task_id, task in self.tasks.items()}
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as f:
            data = json.load(f)
            self.tasks = {
                int(task_id): Task.from_dict(task_data)
                for task_id, task_data in data.items()
            }

    def pretty_print(self, task_list=None):
        if task_list is None:
            task_list = self.list_tasks()
        if not task_list:
            print("No tasks found.")
            return
        table = [
            [task.id, task.description, task.status.value, task.created_at.strftime("%Y-%m-%d %H:%M"), task.updated_at.strftime("%Y-%m-%d %H:%M")]
            for task in task_list
        ]
        print(tabulate(table, headers=["ID", "Description", "Status", "Created At", "Updated At"], tablefmt="fancy_grid"))
