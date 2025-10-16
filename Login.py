from module import *
import json
import os
from datetime import datetime
import getpass
users = {}  #hav chmous users.json

def load_users():
    """Load users from JSON file"""
    global users
    try:
        with open('users.json', 'r') as file:
            data = json.load(file)
            users = data.get('users', {})
    except FileNotFoundError:
        # Create the file if it doesn't exist
        users = {}
        save_users()
    except json.JSONDecodeError:
        print("Error reading user data file!")
        users = {}

def save_users():
    """Save users to JSON file"""
    try:
        data = {
            'users': users,
            'last_updated': datetime.now().isoformat()
        }
        with open('users.json', 'w') as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print(f"Error saving user data: {e}")


def register():
    print("\n--- Register ---")
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists! Try again.")
    else:
        password = getpass.getpass("Enter new password: ")
        # Store additional user info
        user_data = {
            'password': password,
            'created_at': datetime.now().isoformat(),
            'last_login': None
        }
        users[username] = user_data
        save_users()
        print("Registration successful!")


def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if username in users:
        user_data = users[username]
        stored_password = user_data if isinstance(user_data, str) else user_data.get('password')

        if stored_password == password:
            print(f"Login successful! Welcome, {username}")
            if isinstance(user_data, dict):
                users[username]['last_login'] = datetime.now().isoformat()
                save_users()
            while True:
                homepageMenu()
                var = input("\nChoose option: ")
                if not getOption(var):
                    break
        else:
            print("Invalid username or password.")
    else:
        print("Invalid username or password.")



def main(): #Load user pi users.json
    load_users()
    
    while True:
        print("\n==== MENU ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("No option!")

def view_user_info():
    if not users:
        print("No users registered yet.")
        return
    
    print(f"\n--- User Information ---")
    print(f"Total registered users: {len(users)}")
    
    for username, user_data in users.items():
        if isinstance(user_data, dict):
            created = user_data.get('created_at', 'Unknown')[:19].replace('T', ' ')
            last_login = user_data.get('last_login')
            if last_login:
                last_login = last_login[:19].replace('T', ' ')
            else:
                last_login = 'Never logged in'
            
            print(f"\nUser: {username}")
            print(f"  Created: {created}")
            print(f"  Last Login: {last_login}")
        else:
            print(f"\nUser: {username} (Legacy format)")


