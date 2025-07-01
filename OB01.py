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

import datetime