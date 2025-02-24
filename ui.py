import os
import time
import json

# Load data from JSON
with open('comp.json') as f:
    data = json.load(f)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def yes_or_no(prompt):
    while True:
        choice = input(prompt + " (Yes/No): ").lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

def about_us():
    clear_screen()
    print("=" * 50)
    print("About Us")
    print("=" * 50)
    print("E-Commerce Tracker is a simple tool to help you track your e-commerce sales.")
    print("=" * 50)
    
    if yes_or_no("Would you like to return to the main menu?"):
        return
    else:
        print("Exiting program...")
        time.sleep(2)
        exit()

def item_settings():
    while True:
        clear_screen()
        print("=" * 50)
        print("Item Settings")
        print("=" * 50)
        print("1. Preview")
        print("2. Select")
        print("3. Search")
        print("4. Track")
        print("5. Update")
        print("6. Untrack")
        print("7. Back")
        print("=" * 50)

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            clear_screen()
            print("=" * 50)
            print("Preview selected.")
            print("=" * 50)
            
            if len(data['items']) == 0:
                print("No items available to display.")
            else:
                # Display the data in its raw form (whatever it contains)
                for item in data['items']:
                    print(item)  # This will print the entire item (assuming it's a dictionary or list)
            
            print("=" * 50)
            time.sleep(2)
            if yes_or_no("Would you like to go back to Item Settings?"):
                continue
            else:
                break
            
        elif choice == "2":
            clear_screen()
            print("=" * 50)
            print("Select selected.")
            print("=" * 50)
            
            if len(data['items']) == 0:
                print("No items available to display.")
            else:
                # Display the data in its raw form (whatever it contains)
                for item in data['items']:
                    print(item)  # This will print the entire item (assuming it's a dictionary or list)
            
            print("=" * 50)
            
            time.sleep(2)
            if yes_or_no("Would you like to go back to Item Settings?"):
                continue
            else:
                break
        elif choice == "3":
            while True:  
                clear_screen()
                print("=" * 50)
                print("Search selected.")
                print("=" * 50)
                search_term = input("Enter item name to search: ")
                
                found_items = []
                
                for item in data['items']:

                    if isinstance(item, dict):
                        for key, value in item.items():
                            if isinstance(value, str) and search_term.lower() in value.lower():
                                found_items.append(item)
                                break
                    elif isinstance(item, str) and search_term.lower() in item.lower():
                        found_items.append(item)

                if found_items:
                    for item in found_items:
                        print(f"Found item: {item}")  
                else:
                    print("No items found.")
                
                print("=" * 50)

                if yes_or_no("Would you like to search again? If No you will be directed back to Item Settings"):
                    continue
                else:
                    break  
                
        elif choice == "4":
            clear_screen()
            print("=" * 50)
            print("Add Item to Track")
            print("=" * 50)

            print("Available fields in the item:")
            if 'items' in data:
                if len(data['items']) > 0:
                    print("Existing item structure:")
                    for key in data['items'][0].keys():
                        print(f"- {key}")
                else:
                    print("No items in data yet.")
            else:
                print("No items field found in data.")

            print("=" * 50)

            new_item = {}
            while True:
                key = input("Enter the field name (or type 'done' to finish): ")
                
                if key.lower() == 'done':
                    break

                value = input(f"Enter value for '{key}': ")
                new_item[key] = value

            if 'items' not in data:
                data['items'] = []
            
            data['items'].append(new_item)  
            
            print("=" * 50)
            print("Action succesfully executed.")
            print("=" * 50)

            # Option to go back to Item Settings or not
            time.sleep(2)
            if yes_or_no("Would you like to go back to Item Settings?"):
                continue  
            else:
                break  

        elif choice == "5":
            clear_screen()
            print("=" * 50)
            print("Update Item")
            print("=" * 50)
            
            if len(data['items']) == 0:
                print("No items available to update.")
            else:
                # List all available items
                print("Select an item to update:")
                for index, item in enumerate(data['items']):
                    print(f"{index + 1}. {item}")
                
                # User selects an item to update
                item_choice = input("Enter the number of the item you want to update: ")
                
                try:
                    item_choice = int(item_choice) - 1  # Convert to index (0-based)
                    if item_choice < 0 or item_choice >= len(data['items']):
                        print("Invalid item number.")
                        time.sleep(2)
                        continue
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    time.sleep(2)
                    continue
                
                selected_item = data['items'][item_choice]
                print(f"Selected item: {selected_item}")
                
                # Update fields for the selected item
                while True:
                    print("=" * 50)
                    print("Item details:")
                    for key, value in selected_item.items():
                        print(f"{key}: {value}")
                    
                    print("=" * 50)
                    field_to_update = input("Enter the field name you want to update (or 'done' to finish): ")
                    
                    if field_to_update.lower() == 'done':
                        break
                    
                    if field_to_update in selected_item:
                        new_value = input(f"Enter new value for '{field_to_update}' (current: {selected_item[field_to_update]}): ")
                        selected_item[field_to_update] = new_value
                        print(f"Updated '{field_to_update}' to '{new_value}'.")
                    else:
                        print(f"'{field_to_update}' not found in this item. Please try again.")
                    
                    # Option to update more fields or not
                    if not yes_or_no("Would you like to update another field?"):
                        break

            print("=" * 50)
            print("Item successfully updated.")
            print("=" * 50)
            time.sleep(2)
            if yes_or_no("Would you like to go back to Item Settings?"):
                continue
            else:
                break

            
        elif choice == "6":
            clear_screen()
            print("=" * 50)
            print("Untrack Item")
            print("=" * 50)
            
            if len(data['items']) == 0:
                print("No items available to delete.")
            else:
                # List all available items
                print("Select an item to delete:")
                for index, item in enumerate(data['items']):
                    print(f"{index + 1}. {item}")
                
                # User selects an item to delete
                item_choice = input("Enter the number of the item you want to delete: ")
                
                try:
                    item_choice = int(item_choice) - 1  # Convert to index (0-based)
                    if item_choice < 0 or item_choice >= len(data['items']):
                        print("Invalid item number.")
                        time.sleep(2)
                        continue
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    time.sleep(2)
                    continue
                
                selected_item = data['items'][item_choice]
                print(f"Selected item: {selected_item}")
                
                # Confirm deletion
                if yes_or_no(f"Are you sure you want to delete the item '{selected_item}'?"):
                    data['items'].pop(item_choice)  # Remove the item from the list
                    print(f"Item '{selected_item}' has been successfully deleted.")
                else:
                    print(f"Item '{selected_item}' was not deleted.")
                
            print("=" * 50)
            time.sleep(2)
            if yes_or_no("Would you like to go back to Item Settings?"):
                continue
            else:
                break

        elif choice == "7":
            return  # Go back to the previous screen (main menu)
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)

def chat():
    while True:
        clear_screen()
        print("=" * 50)
        print("Chat")
        print("=" * 50)
        print("1. New Chat...")
        print("2. View Existing Chat...")
        print("3. Back")
        print("=" * 50)

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            clear_screen()
            print("=" * 50)
            print("This is a New Chat...")
            print("=" * 50)
            time.sleep(2)
            if yes_or_no("Would you like to go back to Chat?"):
                continue
            else:
                break
        elif choice == "2":
            clear_screen()
            print("=" * 50)
            print("Opening the previous chat...")
            print("=" * 50)
            time.sleep(2)
            if yes_or_no("Would you like to go back to Chat?"):
                continue
            else:
                break
        elif choice == "3":
            return  # Go back to the main menu
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)

def main_menu():
    clear_screen()
    print("=" * 50)
    print("Welcome to E-Commerce Tracker!")
    print("=" * 50)
    print("Press any key to continue")
    input()

    while True:
        clear_screen()
        print("=" * 50)
        print("Main Menu")
        print("=" * 50)
        print("1. About Us")
        print("2. List of Item Settings")
        print("3. Chat")
        print("4. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            about_us()
        elif choice == "2":
            item_settings()
        elif choice == "3":
            chat()
        elif choice == "4":
            clear_screen()
            if yes_or_no("Are you sure you want to exit?"):
                print("Thank you for using E-Commerce Tracker!")
                time.sleep(3)
                break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)

if __name__ == "__main__":
    main_menu()
