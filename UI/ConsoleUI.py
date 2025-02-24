import json
import os
from colorama import init, Fore, Style
from Supermarket.UI.CustomerUI import CustomerUI
from Supermarket.UI.CashierUI import CashierUI
from Supermarket.UI.ShiftManagerUI import ShiftManagerUI
from Supermarket.UI.GeneralManagerUI import GeneralManagerUI
from Supermarket.UI.StockerUI import StockerUI
from Supermarket.utils.file_handler import load_employees, load_sales

# Initialize colorama
init(autoreset=True)

# Load paths from configuration file
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
    data_path = os.path.abspath(os.path.join(os.path.dirname(config_path), config['data_path']))

class ConsoleUI:
    def __init__(self):
        self.employees = load_employees(os.path.join(data_path, 'employees.txt'))
        self.sales = load_sales(os.path.join(data_path, 'sales.txt'))

    def show_menu(self):
        while True:
            print(Fore.GREEN + Style.BRIGHT + "="*50)
            print(Fore.GREEN + Style.BRIGHT + " " * 15 + "Supermarket Management System")
            print(Fore.GREEN + Style.BRIGHT + "="*50)
            print(Fore.CYAN + "1. Customer")
            print(Fore.CYAN + "2. Cashier")
            print(Fore.CYAN + "3. Stocker")
            print(Fore.CYAN + "4. Shift Manager")
            print(Fore.CYAN + "5. General Manager")
            print(Fore.RED + "q. Quit")
            print(Style.RESET_ALL + "="*50)
            option = input(Fore.YELLOW + "Please select an option: ").strip()

            if option == '1':
                self.open_customer_menu()
            elif option == '2':
                self.employee_login('Cashier')
            elif option == '3':
                self.employee_login('Stocker')
            elif option == '4':
                self.employee_login('ShiftManager')
            elif option == '5':
                self.employee_login('GeneralManager')
            elif option.lower() == 'q':
                break
            else:
                print(Fore.RED + "Invalid option. Please try again.")

    def employee_login(self, role):
        while True:
            employee_input = input(Fore.YELLOW + "Enter your employee number (or 'q' to go back): ").strip()
            if employee_input.lower() == 'q':
                return  # Go back to the previous menu

            try:
                employee_number = employee_input  # Keep employee_number as a string
                valid_employee = False
                for employee in self.employees:
                    if employee['employee_number'] == employee_number and employee['role'].lower() == role.lower():
                        valid_employee = True
                        employee_name = employee['name']
                        if role.lower() == 'cashier':
                            cashier_ui = CashierUI(employee_number, employee_name)
                            cashier_ui.display_menu()
                        elif role.lower() == 'stocker':
                            stocker_ui = StockerUI(employee_number, employee_name)
                            stocker_ui.display_menu()
                        elif role.lower() == 'shiftmanager':
                            shift_manager_ui = ShiftManagerUI(employee_number, employee_name)
                            shift_manager_ui.display_menu()
                        elif role.lower() == 'generalmanager':
                            general_manager_ui = GeneralManagerUI(employee_number, employee_name)
                            general_manager_ui.display_menu()
                        return
                if not valid_employee:
                    print(Fore.RED + "Invalid employee number or role.")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid employee number.")

            retry_option = input(Fore.YELLOW + "Do you want to try again? (y/n): ").strip()
            if retry_option.lower() != 'y':
                return  # Exit the method if the user does not want to retry

    def open_customer_menu(self):
        customer_ui = CustomerUI()
        customer_ui.display_menu()
