```python
class ScrumBoard:
    def __init__(self):
        self.backlog = []
        self.sprint_backlog = []
        self.in_progress = []
        self.done = []

    def add_to_backlog(self, task):
        self.backlog.append(task)

    def move_to_sprint_backlog(self, task):
        if task in self.backlog:
            self.backlog.remove(task)
            self.sprint_backlog.append(task)

    def start_task(self, task):
        if task in self.sprint_backlog:
            self.sprint_backlog.remove(task)
            self.in_progress.append(task)

    def complete_task(self, task):
        if task in self.in_progress:
            self.in_progress.remove(task)
            self.done.append(task)


class ScrumTeam:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.scrum_board = ScrumBoard()

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)

    def get_team_status(self):
        return {
            'team_name': self.name,
            'members': self.members,
            'backlog': self.scrum_board.backlog,
            'sprint_backlog': self.scrum_board.sprint_backlog,
            'in_progress': self.scrum_board.in_progress,
            'done': self.scrum_board.done
        }
```