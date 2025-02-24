import datetime
import json
import os
from colorama import init, Fore, Style
from Supermarket.Stuff.Cashier import Cashier
from Supermarket.Stuff.ShiftManager import ShiftManager
from Supermarket.Stuff.Stocker import Stocker
from Supermarket.utils.file_handler import load_employees, save_employees, load_inventory, save_inventory, load_sales, \
    load_products, load_customers

# Initialize colorama
init(autoreset=True)

# Load paths from configuration file
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
    data_path = os.path.abspath(os.path.join(os.path.dirname(config_path), config['data_path']))


class GeneralManagerUI:
    def __init__(self, employee_number, employee_name):
        """Initialize the GeneralManagerUI with the employee's details and load data from files."""
        self.employee_name = employee_name
        self.employee_number = employee_number
        self.employees = load_employees(os.path.join(data_path, 'employees.txt'))
        self.inventory = load_inventory(os.path.join(data_path, 'inventory.txt'))
        self.sales = load_sales(os.path.join(data_path, 'sales.txt'))
        self.products = load_products(os.path.join(data_path, 'products.txt'))

    def display_menu(self):
        """Display the menu for the general manager and handle user input."""
        while True:
            print(Fore.GREEN + Style.BRIGHT + "=" * 50)
            print(Fore.GREEN + Style.BRIGHT + f"Welcome {self.employee_name}")
            print(Fore.GREEN + Style.BRIGHT + "=" * 50)
            print(Fore.CYAN + "1. View All Employees")
            print(Fore.CYAN + "2. Add Employee")
            print(Fore.CYAN + "3. Remove Employee")
            print(Fore.CYAN + "4. View All Products")
            print(Fore.CYAN + "5. View Total Revenue for the Day")
            print(Fore.CYAN + "6. Update Inventory")
            print(Fore.CYAN + "7. View Inventory")
            print(Fore.CYAN + "8. View All Customers")
            print(Fore.CYAN + "9. View Today's Purchases")
            print(Fore.RED + "q. Go Back")
            print(Style.RESET_ALL + "=" * 50)
            choice = input(Fore.YELLOW + "Please select an option: ").strip()

            if choice == '1':
                self.view_employees()
            elif choice == '2':
                self.add_employee()
            elif choice == '3':
                self.remove_employee()
            elif choice == '4':
                self.view_all_products()
            elif choice == '5':
                self.view_total_revenue_for_the_day()
            elif choice == '6':
                self.update_inventory()
            elif choice == '7':
                self.view_inventory()
            elif choice == '8':
                self.view_all_customers()
            elif choice == '9':
                self.view_todays_purchases()
            elif choice == 'q':
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")

    def add_employee(self):
        """Add a new employee to the system."""
        while True:
            print(Fore.GREEN + "\nAdding a New Employee:")
            role = input(
                Fore.YELLOW + "Enter employee role (Cashier, Stocker, Shift Manager, General Manager): ").strip()

            # Validate role
            valid_roles = ['cashier', 'stocker', 'shiftmanager', 'generalmanager']
            if role.lower() not in valid_roles:
                print(Fore.RED + "Invalid role. Please try again.")
                print(Fore.YELLOW + f"Valid roles are: {', '.join([role.capitalize() for role in valid_roles])}")
                continue

            # Set default attributes based on role
            if role.lower() == 'cashier':
                attribute_1, attribute_2 = 'Name Tag', 'Vest'
            elif role.lower() == 'stocker':
                attribute_1, attribute_2 = 'Cap', 'Safety Boots'
            elif role.lower() == 'shiftmanager':
                attribute_1, attribute_2 = 'Walkie-Talkie', 'Tablet'
            elif role.lower() == 'generalmanager':
                attribute_1, attribute_2 = 'Office Key', 'Company Car'

            employee = {
                'employee_number': input(Fore.YELLOW + "Enter employee number: ").strip(),
                'name': input(Fore.YELLOW + "Enter employee name: ").strip(),
                'age': input(Fore.YELLOW + "Enter employee age: ").strip() or '0',
                'phone': input(Fore.YELLOW + "Enter employee phone: ").strip() or 'N/A',
                'role': role,
                'attribute_1': attribute_1,
                'attribute_2': attribute_2
            }
            self.employees.append(employee)
            save_employees(os.path.join(data_path, 'employees.txt'), self.employees)
            print(Fore.GREEN + f"\nEmployee {employee['name']} added successfully.")
            break

    def remove_employee(self):
        """Remove an employee from the system."""
        try:
            employee_number = input(Fore.YELLOW + "Enter employee number to remove: ").strip()
            employee_to_remove = next((emp for emp in self.employees if emp['employee_number'] == employee_number),
                                      None)
            if employee_to_remove:
                if employee_to_remove['role'].lower() in ['cashier', 'stocker', 'shiftmanager'] and employee_to_remove[
                    'role'].lower() != 'generalmanager':
                    self.employees.remove(employee_to_remove)
                    save_employees(os.path.join(data_path, 'employees.txt'), self.employees)
                    print(Fore.GREEN + f"\nEmployee {employee_to_remove['name']} removed successfully.")
                else:
                    print(Fore.RED + "Unauthorized to remove this role.")
            else:
                print(Fore.RED + "Employee not found.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number for employee number.")

    def view_employees(self):
        """Display the list of employees."""
        print(Fore.GREEN + "\nEmployees List:")
        print(
            Fore.YELLOW + "---------------------------------------------------------------------------------------------------")
        print(
            Fore.YELLOW + f"{'Number':<10} {'Name':<20} {'Age':<5} {'Phone':<15} {'Role':<15} {'Attr1':<15} {'Attr2':<15}")
        print(
            Fore.YELLOW + "---------------------------------------------------------------------------------------------------")
        for employee in self.employees:
            print(
                Fore.CYAN + f"{employee['employee_number']:<10} {employee['name']:<20} {employee['age']:<5} {employee['phone']:<15} {employee['role']:<15} {employee['attribute_1']:<15} {employee['attribute_2']:<15}")
        print(
            Fore.YELLOW + "---------------------------------------------------------------------------------------------------")

    def view_all_products(self):
        """Display the list of all products."""
        print(Fore.GREEN + "\nProducts List:")
        print(Fore.YELLOW + "-------------------------------------------------------------------")
        print(Fore.YELLOW + f"{'Product ID':<10} {'Product Name':<30} {'Price':<10}")
        print(Fore.YELLOW + "-------------------------------------------------------------------")
        for prod in self.products:
            print(Fore.CYAN + f"{prod['id']:<10} {prod['name']:<30} {prod['price']:<10.2f}")
        print(Fore.YELLOW + "-------------------------------------------------------------------")

    def view_total_revenue_for_the_day(self):
        """Display the total revenue for the current day."""
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        total_revenue = sum(sale['total'] for sale in self.sales if sale['date'] == current_date)
        print(Fore.GREEN + f"\nTotal revenue for {current_date}: {total_revenue:.2f}")

    def update_inventory(self):
        """Update the inventory with a new quantity for a specified product."""
        print(Fore.GREEN + "\nUpdating Inventory...")
        try:
            product_id = int(input(Fore.YELLOW + "Enter product ID: ").strip())
            new_quantity = int(input(Fore.YELLOW + "Enter new quantity: ").strip())

            if product_id in self.inventory:
                self.inventory[product_id] = new_quantity
                save_inventory(os.path.join(data_path, 'inventory.txt'), self.inventory)
                print(Fore.GREEN + "Inventory updated successfully.")
            else:
                print(Fore.RED + "Product ID not found.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter valid numbers for product ID and quantity.")

    def view_inventory(self):
        """Display the inventory."""
        print(Fore.GREEN + "\nInventory:")
        print(Fore.YELLOW + "-------------------------------------------------------------------")
        print(Fore.YELLOW + f"{'Product ID':<10} {'Quantity':<10}")
        print(Fore.YELLOW + "-------------------------------------------------------------------")
        for prod_id, quantity in self.inventory.items():
            print(Fore.CYAN + f"{prod_id:<10} {quantity:<10}")
        print(Fore.YELLOW + "-------------------------------------------------------------------")

    def view_all_customers(self):
        """Display the list of all customers."""
        customers = load_customers(os.path.join(data_path, 'customers.txt'))
        print(Fore.GREEN + "\nCustomer List:")
        print(Fore.YELLOW + "-------------------------------------------------------------------")
        print(Fore.YELLOW + f"{'Customer ID':<15} {'Name':<30}")
        print(Fore.YELLOW + "-------------------------------------------------------------------")
        for cust in customers:
            print(Fore.CYAN + f"{cust['id']:<15} {cust['name']:<30}")
        print(Fore.YELLOW + "-------------------------------------------------------------------")

    def view_todays_purchases(self):
        """Display today's purchases."""
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        print(Fore.GREEN + "\nToday's Purchases:")
        print(
            Fore.YELLOW + "-----------------------------------------------------------------------------------------------------")
        print(
            Fore.YELLOW + f"{'Cashier ID':<10} {'Product ID':<10} {'Quantity':<10} {'Total':<10} {'Date':<15} {'Customer ID':<12} {'Customer Name':<15}")
        print(
            Fore.YELLOW + "-----------------------------------------------------------------------------------------------------")
        for sale in self.sales:
            if sale['date'] == current_date:
                print(
                    Fore.CYAN + f"{sale['cashier_id']:<10} {sale['product_id']:<10} {sale['quantity']:<10} {sale['total']:<10.2f} {sale['date']:<15} {sale['customer_id']:<12} {sale['customer_name']:<15}")
        print(
            Fore.YELLOW + "-----------------------------------------------------------------------------------------------------")
