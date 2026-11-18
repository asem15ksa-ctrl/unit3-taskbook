"""Command-line interface for Task Tracker."""
from tasks import add_task, complete_task, summary


def show(tasks):
    if not tasks:
        print("No tasks yet.")
    for number, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{number}. [{mark}] {task['title']}")
    print(summary(tasks))


def main():
    tasks = []
    while True:
        print("\n1) Add task  2) List tasks  3) Complete task  4) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_task(tasks, input("Title: "))
            print("Added.")
        elif choice == "2":
            show(tasks)
        elif choice == "3":
            complete_task(tasks, int(input("Task number: ")))
            print("Done.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
