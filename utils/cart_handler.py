import os

def load_cart(filename='data/cart.txt'):
    cart = []
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return cart

    try:
        with open(filename, 'r') as file:
            for line in file:
                if not line.strip():
                    continue  # Skip empty lines
                parts = line.strip().split(',')
                if len(parts) == 4:
                    customer_id, product_id, quantity, status = parts
                    cart.append({'customer_id': customer_id, 'product_id': product_id, 'quantity': int(quantity), 'status': status})
                else:
                    print(f"Unexpected format in line: {line.strip()}")
    except Exception as e:
        print(f"Error loading cart from {filename}: {e}")

    return cart

def save_cart(cart, filename='data/cart.txt'):
    try:
        with open(filename, 'w') as file:
            for item in cart:
                file.write(f"{item['customer_id']},{item['product_id']},{item['quantity']},{item['status']}\\n")
    except Exception as e:
        print(f"Error saving cart to {filename}: {e}")

def add_to_cart(cart, inventory, customer_id, product_id, quantity):
    if product_id in inventory and inventory[product_id] >= quantity:
        inventory[product_id] -= quantity
        cart.append({'customer_id': customer_id, 'product_id': product_id, 'quantity': quantity, 'status': 'in_cart'})
    else:
        print(f"Not enough inventory to add {quantity} units of product {product_id} to cart.")

def view_cart(cart, customer_id):
    return [item for item in cart if item['customer_id'] == customer_id and item['status'] == 'in_cart']

def finalize_purchase(cart, customer_id):
    for item in cart:
        if item['customer_id'] == customer_id and item['status'] == 'in_cart':
            item['status'] = 'purchased'
