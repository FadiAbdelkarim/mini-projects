import json
import argparse

def main():
    parser = argparse.ArgumentParser(description="My CLI Todo Manager")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", help="The task description")
    list_parser = subparsers.add_parser("list", help="List all tasks")
    delete_parser = subparsers.add_parser("delete", help="Delete a task by id")
    delete_parser.add_argument("id", type=int, help="The id of the task to delete")

    args = parser.parse_args()
    if args.command == "add":
        tasks = load_tasks("tasks.json")
        new_id = len(tasks) + 1
        tasks.append({"id": new_id, "task": args.task, "done": False})
        save_tasks("tasks.json", tasks)
        print(f"Added task: {args.task}")
    elif args.command == "list":
        tasks = load_tasks("tasks.json")
        if not tasks:
            print("No tasks yet.")
        else:
            for task in tasks:
                status = "✓" if task["done"] else "✗"
                print(f"[{status}] {task['id']}: {task['task']}")
    elif args.command == "delete":
        tasks = load_tasks("tasks.json")
        task_to_delete = next((task for task in tasks if task["id"] == args.id), None)
        if task_to_delete:
            tasks.remove(task_to_delete)
            save_tasks("tasks.json", tasks)
            print(f"Deleted task with id: {args.id}")
        else:
            print(f"No task found with id: {args.id}")

def load_tasks(filename):

    try:
        with open(filename, "r") as file:
            data = json.load(file)
            
    except FileNotFoundError:
        print("no tasks saved")
        data = []
    return data



def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)
    



    





if __name__ == "__main__":
    main()