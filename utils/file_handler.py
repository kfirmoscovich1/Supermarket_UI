import csv
import os
# Function to load employees from a file
def load_employees(file_path):
    employees = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            employee_data = line.strip().split(',')
            # Ensuring we have the correct number of fields in each line
            if len(employee_data) == 7:
                employees.append({
                    'employee_number': employee_data[0].strip(),
                    'name': employee_data[1].strip(),
                    'age': employee_data[2].strip(),
                    'phone': employee_data[3].strip(),
                    'role': employee_data[4].strip(),
                    'attribute_1': employee_data[5].strip(),
                    'attribute_2': employee_data[6].strip()
                })
            else:
                print(f"Error: Incorrect format in line: {line}")
    return employees

# Function to save employees to a file
def save_employees(file_path, employees):
    with open(file_path, 'w', encoding='utf-8') as file:
        for employee in employees:
            file.write(f"{employee['employee_number']},{employee['name']},{employee['age']},{employee['phone']},{employee['role']},{employee['attribute_1']},{employee['attribute_2']}\n")

# Function to load sales from a file
def load_sales(file_path):
    sales = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Use 'utf-8' encoding
            reader = csv.DictReader(file)
            for line in reader:
                sales.append({
                    'cashier_id': int(line['cashier_id']),
                    'product_id': int(line['product_id']),
                    'quantity': int(line['quantity']),
                    'total': float(line['total']),
                    'date': line['date'],
                    'customer_id': int(line['customer_id']),
                    'customer_name': line['customer_name']
                })
    except UnicodeDecodeError:
        print("Error: Unable to read sales file due to encoding issues.")
    except Exception as e:
        print(f"Error: {e}")
    return sales

# Function to save sales to a file
def save_sales(file_path, sales):
    try:
        with open(file_path, 'w', newline='') as file:
            fieldnames = ['cashier_id', 'product_id', 'quantity', 'total', 'date', 'customer_id', 'customer_name']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for sale in sales:
                writer.writerow(sale)
    except Exception as e:
        print(f"Error saving sales: {e}")

# Function to load products from a file
def load_products(file_path):
    products = []
    with open(file_path, 'r') as file:
        for line in file:
            product_data = line.strip().split(',')
            if len(product_data) != 4:
                print(f"Skipping invalid product data: {line}")
                continue
            try:
                products.append({
                    'id': int(product_data[0].strip()),
                    'name': product_data[1].strip(),
                    'price': float(product_data[2].strip()),
                    'department_id': int(product_data[3].strip())
                })
            except ValueError as e:
                print(f"Error processing line {line}: {e}")
    return products


# Function to load the cart from a file
def load_cart(file_path):
    cart = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    cart_data = line.split(',')
                    try:
                        item = {
                            'product': {
                                'id': int(cart_data[0]),
                                'name': cart_data[1],
                                'price': float(cart_data[2])
                            },
                            'quantity': int(cart_data[3])
                        }
                        cart.append(item)
                    except ValueError:
                        print(f"Invalid cart data: {line}")
    return cart

# Function to save the cart to a file
def save_cart(file_path, cart):
    with open(file_path, 'w') as file:
        for item in cart:
            product = item['product']
            file.write(f"{product['id']},{product['name']},{product['price']},{item['quantity']}\n")

# Function to load inventory from a file
def load_inventory(file_path):
    inventory = {}
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file, fieldnames=['product_id', 'quantity'])
            for row in reader:
                inventory[int(row['product_id'])] = int(row['quantity'])
    except Exception as e:
        print(f"Error loading inventory: {e}")
    return inventory

# Function to save inventory to a file
def save_inventory(file_path, inventory):
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            for product_id, quantity in inventory.items():
                writer.writerow([product_id, quantity])
    except Exception as e:
        print(f"Error saving inventory: {e}")

# Function to load departments from a file
def load_departments(file_path):
    departments = []
    with open(file_path, 'r') as file:
        for line in file:
            department_data = line.strip().split(',')
            departments.append({
                'id': int(department_data[0].strip()),
                'name': department_data[1].strip()
            })
    return departments

# Function to save customers to a file
def save_customers(file_path, customers):
    with open(file_path, 'w', encoding='utf-8') as file:
        for customer in customers:
            file.write(f"{customer['id']},{customer['name']}\n")

# Function to load customers from a file
def load_customers(file_path):
    customers = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            customer_data = line.strip().split(',')
            customers.append({
                'id': int(customer_data[0].strip()),
                'name': customer_data[1].strip()
            })
    return customers
