# This the command line pattern.

from taskmanager import TaskManager
import sys

class Menu:
    """User can select and perform actions from the command line."""
    def __init__(self):
        """ display the use with the list of options and capture the user input
        into variable action. This menu is displayed indefinitely until user chooses
        exit option"""
        #add, view, mask, delete tasks and exit menu.
        tm = TaskManager()
        self.ActionList = {
            "1" : self.AddTasks,
            "2" : self.ViewTasks,
            "3" : self.MaskTasks,
            "4" : self.DeleteTasks,
            "5" : self.ExitTest,
        }

#        while True:
#            print("choose from the below options - please enter the appropirate choice \n")
#            self.run(input("select 1"))

    def display(self):
        """Displays the option to choose for the User."""
        print(""" choose the options below 
            1 : add tasks
            2 : view tasks
            3 : Mask tasks
            4 : Delete tasks
            5 : Exit test
        """)

    def run(self):
        """ Takes the user input and run the appropriate method."""
        while True:
            self.display()
            choice = input() # here we  are not displaying the prompt because it is termed as a functionality.
            action = self.ActionList.get(choice)
            if action:
                action()
            else:
                print("please choose appropriate option 1 to 5.")

    def AddTasks(self):
        """Take the user input from cmdline and call tm module."""
        print("AddTasks.")

    def ViewTasks(self):
        print("ViewTasks.")

    def MaskTasks(self):
        print("MaskTasks.")

    def DeleteTasks(self):
        print("DeleteTasks.")

    def ExitTest(self):
        """Exit the test"""
        sys.exit("Exiting Test.")

if __name__ == "__main__":
    m = Menu()
    m.run()