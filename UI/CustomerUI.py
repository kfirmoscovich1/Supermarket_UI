import json
import os
from colorama import init, Fore, Style
from Supermarket.utils.file_handler import load_products, save_cart, load_cart, load_customers, save_customers, \
    load_departments

# Initialize colorama
init(autoreset=True)

# Load paths from configuration file
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
    data_path = os.path.abspath(os.path.join(os.path.dirname(config_path), config['data_path']))


class CustomerUI:
    def __init__(self):
        """Initialize the CustomerUI with data from files."""
        self.products = load_products(os.path.join(data_path, 'products.txt'))
        self.cart = load_cart(os.path.join(data_path, 'cart.txt'))
        self.customers = load_customers(os.path.join(data_path, 'customers.txt'))
        self.departments = load_departments(os.path.join(data_path, 'departments.txt'))

    def display_menu(self):
        """Display the menu for the customer and handle user input."""
        full_name = input(Fore.YELLOW + "Enter Your Full Name: ").strip()
        if not full_name:
            print(Fore.RED + "Full name cannot be empty.")
            return

        customer_id = self.add_customer(full_name)
        print(Fore.MAGENTA + Style.BRIGHT + "\n" + "=" * 50)
        print(Fore.MAGENTA + Style.BRIGHT + " " * 15 + f"Your Customer ID is: {customer_id}")
        print(Fore.MAGENTA + Style.BRIGHT + "=" * 50)

        while True:
            print(Fore.GREEN + Style.BRIGHT + "=" * 50)
            print(Fore.GREEN + Style.BRIGHT + " " * 20 + "Customer Menu")
            print(Fore.GREEN + Style.BRIGHT + "=" * 50)
            print(Fore.CYAN + "1. View Products")
            print(Fore.CYAN + "2. Add Product to Cart")
            print(Fore.CYAN + "3. View Cart")
            print(Fore.RED + "q. Go Back")
            print(Style.RESET_ALL + "=" * 50)
            choice = input(Fore.YELLOW + "Please select an option: ").strip()
            if choice == '1':
                self.view_products()
            elif choice == '2':
                self.add_product_to_cart()
            elif choice == '3':
                self.view_cart()
            elif choice == 'q':
                break
            else:
                print(Fore.RED + "Invalid option. Please try again.")

    def view_products(self):
        """Display the list of products grouped by departments."""
        departments = {
            'GreenGrocer': [],
            'DryGoods': [],
            'Deli': [],
            'Butchery': []
        }

        # Group products by departments
        for product in self.products:
            department_name = next(
                (dept['name'] for dept in self.departments if dept['id'] == product['department_id']), "Unknown")
            departments[department_name].append(product)

        print(Fore.GREEN + "\nProduct List")
        print("ID | Name        | Price  | Department")
        print("---------------------------------------")

        for dept_name, products in departments.items():
            if products:
                print(Fore.YELLOW + f"\n{dept_name}")
                print("---------------------------------------")
                for product in products:
                    print(f"{product['id']:2} | {product['name']:10} | {product['price']:5.2f}")
                print("---------------------------------------")

    def add_product_to_cart(self):
        """Add a specified product and quantity to the customer's cart."""
        try:
            product_id = int(input(Fore.YELLOW + "Enter product ID to add to cart: ").strip())
            quantity = int(input(Fore.YELLOW + "Enter quantity: ").strip())
            product = next((item for item in self.products if item['id'] == product_id), None)
            if product:
                self.cart.append({'product': product, 'quantity': quantity})
                save_cart(os.path.join(data_path, 'cart.txt'), self.cart)
                print(Fore.GREEN + f"Added {quantity} of {product['name']} to cart.")
            else:
                print(Fore.RED + "Invalid product ID.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter valid numbers for product ID and quantity.")

    def view_cart(self):
        """Display the current items in the customer's cart."""
        if not self.cart:
            print(Fore.YELLOW + "Cart is empty.")
            return
        print(Fore.GREEN + "\nCart Items")
        print("ID | Name        | Price | Quantity")
        print("-----------------------------------")
        for item in self.cart:
            product = item['product']
            print(f"{product['id']:2} | {product['name']:10} | {product['price']:5.2f} | {item['quantity']:8}")
        print("-----------------------------------")

    def add_customer(self, full_name):
        """Add a new customer to the system."""
        customer_id = len(self.customers) + 1
        self.customers.append({'id': customer_id, 'name': full_name})
        save_customers(os.path.join(data_path, 'customers.txt'), self.customers)
        return customer_id
