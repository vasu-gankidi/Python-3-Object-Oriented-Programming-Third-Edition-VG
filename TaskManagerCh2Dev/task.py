from datetime import date

last_id = 0
status = frozenset({"Completed", "NotCompleted"})

class Task:
    """stores the Task information."""
    def __init__(self, title, description = '', status = "NotCompleted"):
        """Create a Task instance and assigns title, creation_datedescription
        ,status and assigns an unique id to each task."""
        self.title = title
        self.description = description
        self.creation_date = date.today()
        self.status = status
        global last_id
        self.TID = last_id + 1
    def Match(self, filter):
        """Matches the task based on the search filter."""
        print("ToDo Future implementation of Match functionality \
              for searching")

if __name__ == "__main__":
    """Test the module when ran individually."""
    task = Task("1", "test1", "Completed")
    print(task.title, task.description, task.creation_date, task.status, task.TID)
    task2 = Task("2", "test2", "Completed")
    print(task2.title, task2.description, task2.creation_date, task2.status, task2.TID)