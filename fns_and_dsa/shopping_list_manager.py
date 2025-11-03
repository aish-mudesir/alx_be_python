# shopping_list_manager.py

def display_menu():
    """Displays the shopping list options menu."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # ✅ Implementation of an array (list) for storing shopping items
    shopping_list = []

    while True:
        # ✅ Calling the display_menu function
        display_menu()

        # ✅ Choice input implemented as a number (integer)
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty.")

        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")

        elif choice == 3:
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()



