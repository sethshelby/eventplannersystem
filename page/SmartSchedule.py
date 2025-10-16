
import json
import os
from datetime import datetime

# Global task storage
tasks = {}

def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            tasks = data.get('tasks', {})
        print(" Tasks loaded successfully!")
        return True
    except FileNotFoundError:
        tasks = {}
        save_tasks()
        return True
    except json.JSONDecodeError:
        print(" Error reading tasks data!")
        tasks = {}
        return False

def save_tasks():
    try:
        data = {
            'tasks': tasks,
            'last_updated': datetime.now().isoformat()
        }
        with open('tasks.json', 'w') as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print(f"❌ Error saving tasks: {e}")

def add_task():
    """Add a new task"""
    print("\n --- Add New Task ---")
    task_name = input("Enter task name: ").strip()
    
    if not task_name:
        print(" Task name cannot be empty!")
        return
    
    if task_name in tasks:
        print(" Task already exists! Use a different name.")
        return
    
    description = input("Enter description: ").strip()
    date_start = input("Enter start date (YYYY-MM-DD): ").strip()
    date_end = input("Enter end date (YYYY-MM-DD): ").strip()
    
    tasks[task_name] = {
        'description': description,
        'date_start': date_start,
        'date_end': date_end,
        'created_at': datetime.now().isoformat()
    }
    
    save_tasks()
    print(f"✅ Task '{task_name}' added successfully!")

def show_tasks():
    """Display all tasks"""
    if not tasks:
        print("\n📋 No tasks added yet.")
        return
    
    print("\n" + "="*70)
    print("📋 ALL TASKS")
    print("="*70)
    
    for task_name, details in tasks.items():
        print(f"\n📌 Task: {task_name}")
        print(f"   📝 Description: {details['description']}")
        print(f"   📅 Start Date: {details['date_start']}")
        print(f"   📅 End Date: {details['date_end']}")
        print("-" * 50)
    
    print("\n Available Tasks:")
    for i, task_name in enumerate(tasks.keys(), 1):
        print(f"{i}. {task_name} (Status: {tasks[task_name]})")


def delete_task():
    """Delete a task"""
    if not tasks:
        print("\n No tasks available to delete.")
        return
    
    print("\n Available Tasks:")
    for i, task_name in enumerate(tasks.keys(), 1):
        print(f"{i}. {task_name}")
    
    task_name = input("\nEnter task name to delete: ").strip()
    
    if task_name not in tasks:
        print(" Task not found!")
        return
    
    confirm = input(f"️  Are you sure you want to delete '{task_name}'? (y/n): ").lower()
    if confirm == 'y':
        del tasks[task_name]
        save_tasks()
        print(f" Task '{task_name}' deleted successfully!")
    else:
        print(" Deletion cancelled.")


def smart_schedule_main():
    load_tasks()
    
    while True:
        print("\n" + "="*50)
        print("📅 SMART SCHEDULE")
        print("="*50)
        print("1. Add Task")
        print("2. Show All Tasks")
        print("4. Delete Task")
        print("0. Back to Main Menu")
        
        choice = input("\n Enter your choice: ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
            input("\nPress Enter to continue...")
        elif choice == "3":
            delete_task()
            input("\n Press Enter to continue...")
        elif choice == "0":
            print(" Returning to main menu...")
            break
        else:
            print(" Invalid choice, try again!")


if __name__ == "__main__":
    smart_schedule_main()