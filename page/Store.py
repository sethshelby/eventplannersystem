
import json
import os
from datetime import datetime


event_stores = {}
shopping_cart = []

def load_event_stores():
    global event_stores
    try:
        with open('event_planner_stores.json', 'r') as file:
            data = json.load(file)
            event_stores = data.get('event_planner_stores', {})
        return True
    except FileNotFoundError:
        print("Event stores data file not found!")
        event_stores = {}
        return False
    except json.JSONDecodeError:
        print("Error reading event stores data!")
        event_stores = {}
        return False

def save_cart_calculation(calculation_data):
    try:
    
        calculations = []
        if os.path.exists('cart_calculations.json'):
            with open('cart_calculations.json', 'r') as file:
                try:
                    calculations = json.load(file)
                except json.JSONDecodeError:
                    calculations = []
        
        
        calculations.append(calculation_data)
        
        
        with open('cart_calculations.json', 'w') as file:
            json.dump(calculations, file, indent=2)
        
        print("Cart calculation saved successfully!")
        return True
    except Exception as e:
        print(f"Error saving calculation: {e}")
        return False

def display_all_stores():
    
    #if not event_stores:
        #print("No stores available. Please load stores first.")
       # return False
    
    
    print("Welcome to Store!")
    print("="*10)
    print("Service Providers:")
    print("-" * 10)
    
    store_count = 1
    for store_id, store_data in event_stores.items():
        category = store_data['category'].replace('_', ' ').title()
        print(f"{store_count}.  {store_data['name']}")
        print(f"Category: {category}")
        print(f"Phone: {store_data['contact']['phone']}")
        print(f"Telegram: {store_data['contact']['telegram']}")
        print()
        store_count += 1
    
    print("0. Back to Main Menu")
    print("="*70)
    return True

def display_store_services(store_key):
    
    if store_key not in event_stores:
        print("Invalid store selection!")
        return False
    
    store = event_stores[store_key]
    category = store['category'].replace('_', ' ').title()
    
    print(f"\n{'='*80}")
    print(f"{store['name']} - {category}")
    print(f"{'='*80}")
    
    
    print("CONTACT INFORMATION:")
    print(f"Phone: {store['contact']['phone']}")
    print(f"Telegram: {store['contact']['telegram']}")
    print(f"Address: {store['contact']['address']}")
    
    
    print(f"\nAVAILABLE SERVICES:")
    print("-" * 50)
    
    for service in store['services']:
        print(f"{service['id']}: {service['name']}")
        print(f"Price: ${service['price']:.2f}")
        print(f"Duration: {service['duration']}")
        
        
        if 'cuisine_type' in service:
            print(f"    Cuisine: {service['cuisine_type']}")
        elif 'theme_type' in service:
            print(f"    Theme: {service['theme_type']}")
        elif 'equipment' in service:
            print(f"    Equipment: {service['equipment']}")
        elif 'service_type' in service:
            print(f"    Service Type: {service['service_type']}")
        
        print(f"Includes: {', '.join(service['includes'])}")
        print()
    
    return True

def add_service_to_cart(store_key, service_id, quantity=1):
    
    if store_key not in event_stores:
        print("Invalid store!")
        return False
    
    store = event_stores[store_key]
    service_found = None
    
    
    for service in store['services']:
        if service['id'].upper() == service_id.upper():
            service_found = service
            break
    
    if not service_found:
        print("Service not found!")
        return False
    
    
    cart_item = {
        'store_id': store_key,
        'store_name': store['name'],
        'store_category': store['category'],
        'store_contact': store['contact'],
        'service_id': service_id.upper(),
        'service_name': service_found['name'],
        'price': service_found['price'],
        'duration': service_found['duration'],
        'quantity': quantity,
        'total_price': service_found['price'] * quantity,
        'includes': service_found['includes']
    }
    
  
    if 'cuisine_type' in service_found:
        cart_item['cuisine_type'] = service_found['cuisine_type']
    elif 'theme_type' in service_found:
        cart_item['theme_type'] = service_found['theme_type']
    elif 'equipment' in service_found:
        cart_item['equipment'] = service_found['equipment']
    elif 'service_type' in service_found:
        cart_item['service_type'] = service_found['service_type']
    
    shopping_cart.append(cart_item)
    
    print(f"Added {quantity}x {service_found['name']} to cart!")
    print(f"Item total: ${cart_item['total_price']:.2f}")
    return True

def view_shopping_cart():
  
    if not shopping_cart:
        print("\nYour shopping cart is empty!")
        return 0
    
    
    print("Shopping Cart:")
    print(f"{'='*80}")
    
    total_cost = 0
    categories = {}
    
    for i, item in enumerate(shopping_cart, 1):
        print(f"\n{i}. {item['service_name']} x{item['quantity']}")
        print(f"Provider: {item['store_name']}")
        print(f"Contact: {item['store_contact']['phone']} | {item['store_contact']['telegram']}")
        print(f"Duration: {item['duration']}")
        
     
        if 'cuisine_type' in item:
            print(f"Cuisine: {item['cuisine_type']}")
        elif 'theme_type' in item:
            print(f"Theme: {item['theme_type']}")
        elif 'equipment' in item:
            print(f"Equipment: {item['equipment']}")
        elif 'service_type' in item:
            print(f"Service Type: {item['service_type']}")
        
        print(f"Includes: {', '.join(item['includes'])}")
        print(f"Cost: ${item['total_price']:.2f}")
        
        total_cost += item['total_price']
        

        category = item['store_category'].replace('_', ' ').title()
        if category not in categories:
            categories[category] = {'cost': 0, 'items': 0}
        categories[category]['cost'] += item['total_price']
        categories[category]['items'] += item['quantity']
    

    
    print(f"\nCategory Breakdown:")
    print("-" * 45)
    
    for category, data in categories.items():
        percentage = (data['cost'] / total_cost) * 100
        print(f"{category}: ${data['cost']:.2f} ({data['items']} items, {percentage:.1f}%)")
    
  
    print(f"\nTOTAL EVENT COST: ${total_cost:.2f}")
    print(f"Total Services: {len(shopping_cart)}")
    print(f"{'='*80}")
    
    return total_cost

def calculate_total_cost():
    
    if not shopping_cart:
        print("No services in cart to calculate!")
        return 0
    
    total_cost = view_shopping_cart()
    
    print(f"\n FINAL COST CALCULATION")
    print(f"{'='*50}")
    print(f"Services in Cart: {len(shopping_cart)}")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"{'='*50}")
    
    
    save_choice = input("\nSave this calculation? (y/n): ").lower().strip()
    if save_choice == 'y':
        event_name = input("Enter event name (optional): ").strip()
        
        calculation_data = {
            'timestamp': datetime.now().isoformat(),
            'event_name': event_name if event_name else f"Event_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'services': shopping_cart.copy(),
            'total_cost': total_cost,
            'service_count': len(shopping_cart),
            'categories': {}
        }
        
        
        for item in shopping_cart:
            category = item['store_category']
            if category not in calculation_data['categories']:
                calculation_data['categories'][category] = {'cost': 0, 'count': 0}
            calculation_data['categories'][category]['cost'] += item['total_price']
            calculation_data['categories'][category]['count'] += item['quantity']
        
        save_cart_calculation(calculation_data)
    
    
    clear_choice = input("Clear cart for new calculation? (y/n): ").lower().strip()
    if clear_choice == 'y':
        shopping_cart.clear()
        print("Cart cleared!")
    
    return total_cost

def view_saved_calculations():
    
    try:
        if not os.path.exists('cart_calculations.json'):
            print("No saved calculations found!")
            return
        
        with open('cart_calculations.json', 'r') as file:
            calculations = json.load(file)
        
        if not calculations:
            print("No saved calculations found!")
            return
        
        print(f"\n{'='*70}")
        print("SAVED EVENT CALCULATIONS")
        print(f"{'='*70}")
        
        for i, calc in enumerate(calculations, 1):
            timestamp = calc['timestamp'][:19].replace('T', ' ')
            event_name = calc.get('event_name', f'Event #{i}')
            
            print(f"\n{i}.{event_name}")
            print(f"Date: {timestamp}")
            print(f"Services: {calc['service_count']}")
            print(f"Total Cost: ${calc['total_cost']:.2f}")
            
            
            if 'categories' in calc:
                print("Categories:", end=" ")
                cat_list = [f"{cat.replace('_', ' ').title()}(${data['cost']:.0f})" 
                           for cat, data in calc['categories'].items()]
                print(", ".join(cat_list))
        
        print(f"\n{'='*70}")
        
        
        detail_choice = input("View details of a calculation? (Enter number or 'n'): ").strip()
        if detail_choice.isdigit():
            calc_num = int(detail_choice) - 1
            if 0 <= calc_num < len(calculations):
                show_calculation_details(calculations[calc_num])
        
    except Exception as e:
        print(f"Error loading saved calculations: {e}")

def show_calculation_details(calculation):
    
    event_name = calculation.get('event_name', 'Unnamed Event')
    timestamp = calculation['timestamp'][:19].replace('T', ' ')
    
    print(f"\n{'='*80}")
    print(f"{event_name.upper()} - DETAILED BREAKDOWN")
    print(f"Calculated on: {timestamp}")
    print(f"{'='*80}")
    
    for i, service in enumerate(calculation['services'], 1):
        print(f"\n{i}. {service['service_name']} x{service['quantity']}")
        print(f"Provider: {service['store_name']}")
        print(f"Contact: {service['store_contact']['phone']} | {service['store_contact']['telegram']}")
        print(f"Duration: {service['duration']}")
        print(f"Includes: {', '.join(service['includes'])}")
        print(f"Cost: ${service['total_price']:.2f}")
    
    print(f"\n{'='*80}")
    print(f"TOTAL: ${calculation['total_cost']:.2f}")
    print(f"{'='*80}")

def event_planner_main():
    
    if not load_event_stores():
        print("Could not load event stores. Please check the data file.")
        return
    
    while True:
        if not display_all_stores():
            break
        
        choice = input(f"\nSelect store (0 to go back): ").strip()
        
        if choice == '0':
            break
        elif choice.isdigit():
            store_index = int(choice) - 1
            store_keys = list(event_stores.keys())
            
            if 0 <= store_index < len(store_keys):
                selected_store = store_keys[store_index]
                store_menu(selected_store)
            else:
                print("Invalid store number!")
        else:
            print("Invalid choice! Please enter a number.")

def store_menu(store_key):
    
    while True:
        if not display_store_services(store_key):
            break
        
        print(f"\n STORE OPTIONS:")
        print("1. Add service to cart")
        print("2. View shopping cart")
        print("3. Calculate total cost")
        print("4. View saved calculations")
        print("0. Back to store selection")
        
        action = input(f"\n Choose action: ").strip()
        
        if action == '0':
            break
        elif action == '1':
            service_id = input("Enter service ID: ").strip()
            if service_id:
                try:
                    quantity = int(input("Enter quantity (default 1): ").strip() or "1")
                    if quantity > 0:
                        add_service_to_cart(store_key, service_id, quantity)
                    else:
                        print("Quantity must be positive!")
                except ValueError:
                    print("Invalid quantity! Please enter a number.")
            else:
                print("Service ID cannot be empty!")
        elif action == '2':
            view_shopping_cart()
            input("\n Press Enter to continue...")
        elif action == '3':
            calculate_total_cost()
            input("\n Press Enter to continue...")
        elif action == '4':
            view_saved_calculations()
            input("\n Press Enter to continue...")



