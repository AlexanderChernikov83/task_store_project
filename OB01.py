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


#Шаг 3

# --- Работа с задачами ---
manager = TaskManager()
manager.add_task("Сделать домашку по Python", "2025-06-15")
manager.add_task("Пройти урок на платформе", "2025-06-16")
manager.add_task("Отправить отчет", "2025-06-17")

manager.complete_task(0)

manager.show_active_tasks()


# --- Работа с магазинами ---
store1 = Store("Фруктовый рай", "ул. Яблочная, 1")
store2 = Store("Зеленый уголок", "ул. Банановая, 5")
store3 = Store("Овощной мир", "ул. Картофельная, 10")

store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.8)

store2.add_item("апельсины", 0.9)
store2.add_item("мандарины", 1.1)

store3.add_item("картошка", 0.4)
store3.add_item("лук", 0.3)

# Тестирование методов
print("\n📦", store1)
print("Цена на бананы:", store1.get_price("бананы"))

store1.update_price("бананы", 0.75)
print("Новая цена на бананы:", store1.get_price("бананы"))

store1.remove_item("яблоки")
print("Цена на яблоки после удаления:", store1.get_price("яблоки"))
