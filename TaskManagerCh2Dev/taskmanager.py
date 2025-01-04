from sys import exception
from task import Task

class TaskManager:
    """Managing task related activities i.e.add, view, mark and delete tasks"""
    def __init__(self):
        """Initialize an attribute of TaskManager holding list Task objects."""
        self.Tasks=[]

    def AddTasks(self, title, description = '', status = "NotCompleted"):
        """Create the task with title, descrption and mark the status."""
        # title mandatory? if yes - add title / no raise exception
        # description optional. if yes - add desc/ no add empty description.
        # status - check if status string is acceptable
        # if yes - add status / no add Not Completed.
        # return status and TID.
        
        # add exception handling here (title, and status).
        # error Task ID is not incrementing. - testing function by function.
        if(title):
            self.Tasks.append(Task(title, description, status))
        
        print("inside add task")
        for taskobj in self.Tasks:
            print("The task title ${0} and TaskId ${1} created", taskobj.title, taskobj.TID)
        
        return True

    def ViewTasks(self, TID):
        """View the task based on the task id"""
        #check if task id (Int) is relevant. yes proceed, no raise exception to check again.
        # if yes - check if tid is present from list of Tasks, 
        # return the title, description and status.
        # if no - return no task present.

        for taskobj in self.Tasks:
            if taskobj.TID == TID:
                print("viewing task ${0} ${1}" , taskobj.title , taskobj.TID)
                return taskobj.title, taskobj.description, taskobj.status
            else:
                return None

    def MaskTask(self, TID):
        """TODO write the code"""
        print("Task is hidden can not display the content of task " , TID)

    def DeleteTask(self, TID):
        """Delete the task based on task id"""
        #for task.TID in self.Tasks, if task.TID=TID delete task
        #check if TID is in correct format, if no task ID present raise execption not found.
        print("Task is deleted" , TID)

if __name__ == "__main__":
    TM = TaskManager()
    TM.AddTasks("Test", "Test Task doing good", "Completed") # user enters the info from cmdline
    TM.ViewTasks(1) # user enter task id from cmdline
    TM.MaskTask(1) # user enter task id from cmdline
    TM.DeleteTask(1) # user enter task id from cmdline