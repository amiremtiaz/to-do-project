import datetime
import os


class ToDo:
    def __init__(self):
        self.todo_list = []
    @staticmethod
    def show_date():
        x = datetime.datetime.now()
        print(x.year , x.month, x.day)

    def show_do_list(self):
        with open("doList.py", "r") as f:
            if os.path.getsize("doList.py") == 0:
                print("Nothing to show!")
            else:
                self.todo_list = f.readlines()
                for i, todo in enumerate(self.todo_list, start = 1):
                    print(f"{i}. {todo}")
    @staticmethod
    def add_todo():
        todo = input("Write your todo : ")
        if todo == "":
            print("Nothing to do!")
        else:
            with open("doList.py", "a") as f:
                f.write(f"{todo}\n")

                print("todo added successfully!")

    def delete_todo(self):
        self.show_do_list()
        try:
            num = int(input("Choose your todo :"))
        except ValueError:
            print("Please enter a number.")
            return
        if num > len(self.todo_list):
            return print("Invalid choice!")
        with open("doList.py", "r") as f:
            lines = f.readlines()
        with open("doList.py", "w") as f:
            for line in lines:
                if line.strip() != self.todo_list[num - 1].strip():
                    f.write(line)
        print("deleted successfully! ")

    def edit_todo(self):
        self.show_do_list()
        lines = []
        try:
            num = int(input("Choose your todo : "))
        except ValueError:
            print("Please enter a number.")
            return
        if num > len(self.todo_list):
            return print("Invalid choice!")
        todo = input("Write your todo : ")
        with open("doList.py", "r") as f:
            lines = f.readlines()
        with open("doList.py", "w") as f:
            for line in lines:
                if line.strip() != self.todo_list[num - 1].strip():
                    f.write(line)
                else:
                    f.write(todo)
        print("edited successfully!")
