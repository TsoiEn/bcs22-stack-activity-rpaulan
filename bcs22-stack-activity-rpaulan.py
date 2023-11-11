"""
Create a task manager in python using stack with basic functionalities:
 (classes, methods, lists, loops, input-handling in python )
 - add tasks with a title and descriptiom
 - mark tasks as completed
 - display the list of tasks along with status
 - exit option to exit the task manager
 push in your gitHub account and paste the URL in our SB- lab
 bcs21-stack-activity-ffernandez.py
 """


# implementation of task manager
class TaskManager:
    def __init__(self):
        # empty stack
        self.tasks = []


    # adding tasks to stack
    def push(self, title, description):
        self.tasks.append({"title": title, "description": description, "completed": False})
        print(f"Task '{title}' added to the Task Manager")

    # removing the tasks from any side of the index
    def pop(self):
        if self.tasks:
            index = int(input("Enter the index of the task you want to remove: "))
            task = self.tasks.pop()
            print(f"Task '{task['title']}' removed.")

            if index is not None:
                if 0 <= index < len(self.tasks):
                    task = self.tasks.pop(index)
                    print(f"Task '{task['title']}' removed.")
            else:
                print("Invalid index. Please enter a valid index.")
        
        else:
            print("No tasks to remove.")

    def update_status(self, title):
        for task in self.tasks:
            if task['title'] == title:
                task['completed'] = True
                print(f"\nTask '{title}' marked as completed.")
                return
        print(f"\nTask '{title}' not found.")

    def display_tasks(self):
        if not self.tasks:
            print("\nNo tasks to display.")
        else:
            print("\nTasks:")
            print("{:<10} {:<20} {:<40} {:<15}".format("Index", "Title", "Description", "Status"))
            for index, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print("{:<10} {:<20} {:<40} {:<15}".format(str(index), task['title'], task['description'], status))
    def main(self):
        while True:
            print("\n----------Task Manager----------")
            print('(1) add tasks')
            print('(2) mark tasks status')
            print('(3) remove tasks')
            print('(4) display task/s')
            print('(5) exit task manager')

            choice = input("Enter choice: ")

            if choice == '1':
                title = input("\nEnter title of the task: ")
                description = input("Enter Description of the task: ")
                self.push(title, description)
            elif choice == '2':
                title = input("\nEnter title of the task to mark as completed: ")
                self.update_status(title)
            elif choice == '3':
                self.pop()
            elif choice == '4':
                self.display_tasks()
            elif choice == '5':
                print("\nthanks for using this task manager.")
                break
            else:
                print("\nInvalid choice. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.main()

