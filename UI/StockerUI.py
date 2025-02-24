import json
import os
from colorama import init, Fore, Style
from Supermarket.utils.file_handler import (
    load_employees,
    load_products,
    load_inventory,
    save_inventory
)

# Initialize colorama
init(autoreset=True)

# Load paths from configuration file
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
    data_path = os.path.abspath(os.path.join(os.path.dirname(config_path), config['data_path']))

class StockerUI:
    def __init__(self, employee_number, employee_name):
        """Initialize the StockerUI with the employee's details and load data from files."""
        self.employee_name = employee_name
        self.employee_number = employee_number
        self.employees = load_employees(os.path.join(data_path, 'employees.txt'))
        self.products = load_products(os.path.join(data_path, 'products.txt'))
        self.inventory = load_inventory(os.path.join(data_path, 'inventory.txt'))

    def display_menu(self):
        """Display the menu for the stocker and handle user input."""
        while True:
            print(Fore.GREEN + Style.BRIGHT + "="*50)
            print(Fore.GREEN + Style.BRIGHT + f"Hello {self.employee_name}")
            print(Fore.GREEN + Style.BRIGHT + "="*50)
            print(Fore.CYAN + "1. View Inventory")
            print(Fore.CYAN + "2. Add to Inventory")
            print(Fore.CYAN + "3. Remove from Inventory")
            print(Fore.RED + "q. Go Back")
            print(Style.RESET_ALL + "="*50)
            choice = input(Fore.YELLOW + "Please select an option: ").strip()

            if choice == '1':
                self.view_inventory()
            elif choice == '2':
                self.add_to_inventory()
            elif choice == '3':
                self.remove_from_inventory()
            elif choice == 'q':
                break
            else:
                print(Fore.RED + "Invalid choice, please try again.")

    def view_inventory(self):
        """Display the current inventory."""
        print(Fore.GREEN + "\nInventory List:")
        print(Fore.YELLOW + "-------------------------------------------------------------------")
        print(Fore.YELLOW + f"{'Product ID':<10} {'Name':<20} {'Quantity':<10}")
        print(Fore.YELLOW + "-------------------------------------------------------------------")
        if isinstance(self.inventory, dict):
            for product_id, quantity in self.inventory.items():
                product = next((p for p in self.products if p['id'] == product_id), None)
                if product:
                    print(Fore.CYAN + f"{product_id:<10} {product['name']:<20} {quantity:<10}")
        else:
            print(Fore.RED + "Error: Inventory data is not in the correct format.")
        print(Fore.YELLOW + "-------------------------------------------------------------------")

    def add_to_inventory(self):
        """Add a specified quantity of a product to the inventory."""
        try:
            product_id = int(input(Fore.YELLOW + "Enter product ID to add to inventory: ").strip())
            quantity = int(input(Fore.YELLOW + "Enter quantity to add: ").strip())
            if isinstance(self.inventory, dict):
                if product_id in self.inventory:
                    self.inventory[product_id] += quantity
                else:
                    self.inventory[product_id] = quantity
                save_inventory(os.path.join(data_path, 'inventory.txt'), self.inventory)
                print(Fore.GREEN + f"Added {quantity} to product ID {product_id}.")
            else:
                print(Fore.RED + "Error: Inventory data is not in the correct format.")
        except ValueError:
            print(Fore.RED + "Error: Please enter valid numbers for product ID and quantity.")

    def remove_from_inventory(self):
        """Remove a specified quantity of a product from the inventory."""
        try:
            product_id = int(input(Fore.YELLOW + "Enter product ID to remove from inventory: ").strip())
            quantity = int(input(Fore.YELLOW + "Enter quantity to remove: ").strip())
            if isinstance(self.inventory, dict):
                if product_id in self.inventory and self.inventory[product_id] >= quantity:
                    self.inventory[product_id] -= quantity
                    save_inventory(os.path.join(data_path, 'inventory.txt'), self.inventory)
                    print(Fore.GREEN + f"Removed {quantity} from product ID {product_id}.")
                else:
                    print(Fore.RED + "Invalid product ID or quantity.")
            else:
                print(Fore.RED + "Error: Inventory data is not in the correct format.")
        except ValueError:
            print(Fore.RED + "Error: Please enter valid numbers for product ID and quantity.")
