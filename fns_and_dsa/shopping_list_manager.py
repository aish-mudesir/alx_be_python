# shopping_list_manager.py

def display_menu():
    """
    Displays the menu options for the Shopping List Manager.
    """
    print("\n===== Shopping List Manager =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("===============================")

def main():
    # Initialize an empty array (list) to store shopping items
    shopping_list = []

    # Loop until the user chooses to exit
    while True:
        # Display the menu to the user
        display_menu()

        # Get user's choice and validate it's a number
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 4.")
            continue

        # Option 1: Add item
        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to your shopping list.")
            else:
                print("⚠️ Item name cannot be empty.")

        # Option 2: Remove item
        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' has been removed from your shopping list.")
            else:
                print(f"⚠️ '{item}' not found in your shopping list.")

        # Option 3: View list
        elif choice == 3:
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("📭 Your shopping list is currently empty.")

        # Option 4: Exit program
        elif choice == 4:
            print("👋 Goodbye! Thanks for using the Shopping List Manager.")
            break

        # Handle invalid menu numbers
        else:
            print("❌ Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()


