# Менеджер задач
#Шаг 1
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✅ Выполнено" if self.completed else "❌ Не выполнено"
        return f"{self.description} (до {self.deadline}) — {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def show_active_tasks(self):
        print("\n🔸 Текущие задачи:")
        for task in self.tasks:
            if not task.completed:
                print(task)


#Шаг 2

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def get_price(self, name):
        return self.items.get(name)

    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price

    def __str__(self):
        return f"{self.name} — {self.address}"
