import datetime
import json
import os
from colorama import init, Fore, Style
from Supermarket.utils.file_handler import load_cart, save_sales, save_cart, load_sales, load_customers

# Initialize colorama
init(autoreset=True)

# Load paths from configuration file
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
    data_path = os.path.abspath(os.path.join(os.path.dirname(config_path), config['data_path']))

class CashierUI:
    def __init__(self, employee_number, employee_name):
        """Initialize the CashierUI with the employee's details and load data from files."""
        self.employee_name = employee_name
        self.employee_number = employee_number
        self.cart = load_cart(os.path.join(data_path, 'cart.txt'))
        self.sales = load_sales(os.path.join(data_path, 'sales.txt'))

    def display_menu(self):
        """Display the menu for the cashier and handle user input."""
        while True:
            print(Fore.GREEN + Style.BRIGHT + "="*50)
            print(Fore.GREEN + Style.BRIGHT + f"Welcome {self.employee_name}")
            print(Fore.GREEN + Style.BRIGHT + "="*50)
            print(Fore.CYAN + "1. Process a Sale")
            print(Fore.CYAN + "2. View Cart")
            print(Fore.CYAN + "3. Remove Item from Cart")
            print(Fore.RED + "q. Go Back")
            print(Style.RESET_ALL + "="*50)
            choice = input(Fore.YELLOW + "Please select an option: ").strip()

            if choice == '1':
                self.process_sale()
            elif choice == '2':
                self.view_cart()
            elif choice == '3':
                self.remove_item_from_cart()
            elif choice == 'q':
                break
            else:
                print(Fore.RED + "Invalid option. Please try again.")

    def process_sale(self):
        """Process the sale for the items currently in the cart."""
        if not self.cart:
            print(Fore.YELLOW + "Cart is empty.")
            return

        print(Fore.GREEN + "Processing sale for the cart items...")
        total = 0
        for item in self.cart:
            product = item['product']
            total += product['price'] * item['quantity']

        if total > 0:
            try:
                customer_id = int(input(Fore.YELLOW + "Enter customer ID: ").strip())
                current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                for item in self.cart:
                    product = item['product']
                    sale_record = {
                        'cashier_id': self.employee_number,
                        'product_id': product['id'],
                        'quantity': item['quantity'],
                        'total': product['price'] * item['quantity'],
                        'date': current_date,
                        'customer_id': customer_id,
                        'customer_name': self.get_customer_name(customer_id)
                    }
                    self.sales.append(sale_record)
                save_sales(os.path.join(data_path, 'sales.txt'), self.sales)
                self.cart = []  # Clear the cart after processing sale
                save_cart(os.path.join(data_path, 'cart.txt'), self.cart)
                print(Fore.GREEN + "Sale processed successfully!")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid customer ID.")
        else:
            print(Fore.RED + "Cart is empty.")

    def view_cart(self):
        """Display the current items in the cart."""
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

    def remove_item_from_cart(self):
        """Remove a specified quantity of a product from the cart."""
        try:
            product_id = int(input(Fore.YELLOW + "Enter product ID to remove from cart: ").strip())
            quantity = int(input(Fore.YELLOW + "Enter quantity to remove: ").strip())
            for item in self.cart:
                if item['product']['id'] == product_id:
                    if item['quantity'] > quantity:
                        item['quantity'] -= quantity
                    elif item['quantity'] == quantity:
                        self.cart.remove(item)
                    else:
                        print(Fore.RED + "Invalid quantity.")
                    break
            save_cart(os.path.join(data_path, 'cart.txt'), self.cart)
            print(Fore.GREEN + "Item removed from cart.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter valid numbers for product ID and quantity.")

    def get_customer_name(self, customer_id):
        """Retrieve the name of a customer given their ID."""
        customers = load_customers(os.path.join(data_path, 'customers.txt'))
        customer = next((c for c in customers if c['id'] == customer_id), None)
        if customer:
            return customer['name']
        else:
            return "Unknown"
