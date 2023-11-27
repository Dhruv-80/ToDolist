import os
import json
import argparse

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        json.dump(todos, file, indent=2)

def list_todos():
    todos = load_todos()
    if todos:
        print("Your TODO list:")
        for idx, todo in enumerate(todos, 1):
            print(f"{idx}. {todo}")
    else:
        print("Your TODO list is empty.")

def add_todo(task):
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    print(f"Added: {task}")

def remove_todo(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        removed_task = todos.pop(index - 1)
        save_todos(todos)
        print(f"Removed: {removed_task}")
    else:
        print("Invalid index. Please provide a valid index.")

def main():
    parser = argparse.ArgumentParser(description="Simple TODO list manager.")
    parser.add_argument('--list', action='store_true', help='List all todos')
    parser.add_argument('--add', type=str, help='Add a new todo')
    parser.add_argument('--remove', type=int, help='Remove a todo by index')

    args = parser.parse_args()

    if args.list:
        list_todos()
    elif args.add:
        add_todo(args.add)
    elif args.remove:
        remove_todo(args.remove)
    else:
        print("Please provide a valid command. Use --help for usage information.")

if __name__ == "__main__":
    main()
