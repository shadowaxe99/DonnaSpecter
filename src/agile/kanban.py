```python
class KanbanBoard:
    def __init__(self):
        self.columns = ['Backlog', 'In Progress', 'Review', 'Done']
        self.tasks = {column: [] for column in self.columns}

    def add_task(self, column, task):
        if column in self.columns:
            self.tasks[column].append(task)
        else:
            print(f"Invalid column. Please choose from {self.columns}")

    def move_task(self, task, from_column, to_column):
        if from_column in self.columns and to_column in self.columns:
            if task in self.tasks[from_column]:
                self.tasks[from_column].remove(task)
                self.tasks[to_column].append(task)
            else:
                print(f"Task not found in {from_column}")
        else:
            print(f"Invalid column. Please choose from {self.columns}")

    def display_board(self):
        for column in self.columns:
            print(f"{column}: {self.tasks[column]}")

# Example usage
kanban = KanbanBoard()
kanban.add_task('Backlog', 'Implement GPT-4 model')
kanban.add_task('Backlog', 'Integrate Google Calendar API')
kanban.move_task('Implement GPT-4 model', 'Backlog', 'In Progress')
kanban.display_board()
```