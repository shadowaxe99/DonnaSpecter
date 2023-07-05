```python
import datetime

class Conflict:
    def __init__(self, conflict_id, parties_involved, conflict_description, conflict_status="Unresolved"):
        self.conflict_id = conflict_id
        self.parties_involved = parties_involved
        self.conflict_description = conflict_description
        self.conflict_status = conflict_status
        self.conflict_resolution = None
        self.resolution_date = None

    def resolve_conflict(self, resolution):
        self.conflict_status = "Resolved"
        self.conflict_resolution = resolution
        self.resolution_date = datetime.datetime.now()

class ConflictResolution:
    def __init__(self):
        self.conflicts = []

    def add_conflict(self, conflict):
        self.conflicts.append(conflict)

    def resolve_conflict(self, conflict_id, resolution):
        for conflict in self.conflicts:
            if conflict.conflict_id == conflict_id:
                conflict.resolve_conflict(resolution)
                return f"Conflict {conflict_id} has been resolved."
        return f"No conflict with ID {conflict_id} found."

    def get_unresolved_conflicts(self):
        return [conflict for conflict in self.conflicts if conflict.conflict_status == "Unresolved"]

    def get_resolved_conflicts(self):
        return [conflict for conflict in self.conflicts if conflict.conflict_status == "Resolved"]
```