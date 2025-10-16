from page.Store import *
from page.SmartSchedule import smart_schedule_main


def homepageMenu():
    print("\n=== MAIN MENU ===")
    print("1. Stores")
    print("2. Smart Schedule")
    print("3. Budget")
    print("4. Profile")
    print("5. Customer")
    print("6. Exit")


def getOption(opt):
    if opt == '1':
        print("\n🏪 --- Event Planner Stores ---")
        event_planner_main()
    elif opt == '2':
        print("\n📅 --- Smart Schedule ---")
        smart_schedule_main()
    elif opt == '3':
        print("\n💰 --- Budget ---")
        print("Budget management features coming soon!")
        input("Press Enter to continue...")
    elif opt == '4':
        print("👋 Thank you for using our Event Planner System!")
        return False  
    else:
        print("❌ Invalid option! Please choose 1-6.")
    return True


