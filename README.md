### MADE BY
- Avi Mahari | Nikita Sayenko | Kfir Moscovich


# Supermarket Application

## Introduction
This project simulates a supermarket system with different roles and functionalities, including customers, cashiers, stockers, shift managers, and main managers. The system allows various interactions such as purchasing products, managing inventory, and handling employee records.

## Requirements
- Python 3.8 or above
- JSON library (built-in)
- Colorama library
- Basic understanding of object-oriented programming concepts such as classes, inheritance, abstraction, and polymorphism.

## Installation
Before running the application, ensure you have the required libraries installed. You can install the required libraries using the following command:

```sh
pip install colorama
```

If using a virtual environment, activate it first:

```sh
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

## Project Structure
The project is organized into several directories and files, each serving a specific purpose:

- **`Main.py`**: The entry point of the application.
- **`config.json`**: Configuration file containing initial data and settings.
- **`data/`**: Directory containing data files.
- **`Departments/`**: Contains code related to different supermarket departments.
- **`Product/`**: Manages product-related functionalities.
- **`Stuff/`**: Contains classes and methods related to supermarket staff.
- **`UI/`**: Handles the user interface and menu displays.
- **`utils/`**: Utility functions used across the project.

## How to Run the Application
1. Ensure you have Python 3.8 or above installed on your machine.
2. Install the required libraries using the installation command mentioned above.
3. Navigate to the directory containing `Main.py`.
4. Run the application using the following command:
   ```sh
   python Main.py
   ```
5. The application will start and display the main menu.

## User Interface
Upon starting the application, a console-based user interface will be presented. Users can navigate through different menus based on their roles in the supermarket. Each role has specific functionalities, which are accessible through the respective menus.

### Main Menu
- **Customer Menu**: Allows customers to view products, add products to their shopping list, and complete purchases.
- **Cashier Menu**: Enables cashiers to process customer purchases and manage transactions.
- **Stocker Menu**: Allows stockers to add or remove products from the inventory.
- **Shift Manager Menu**: Provides functionalities to manage employees, view customer purchases, and update inventory.
- **Main Manager Menu**: Includes all functionalities available to shift managers, along with additional capabilities to view overall sales and manage high-level operations.

## Functionalities

### Customer Menu
- **View Products**: Displays a list of products available on the shelves.
- **Add to Shopping List**: Allows customers to add products to their shopping list.
- **Complete Purchase**: Processes the customer's shopping list and finalizes the purchase.

### Cashier Menu
- **Process Purchase**: Handles the transaction process for customer purchases.
- **View Sales**: Displays a list of sales processed by the cashier.

### Stocker Menu
- **Add Products**: Allows stockers to add new products to the inventory.
- **Remove Products**: Enables stockers to remove products from the inventory.

### Shift Manager Menu
- **Manage Employees**: Add, update, or remove employee records.
- **View Customer Purchases**: Displays a list of customer purchases for the day.
- **Update Inventory**: Allows shift managers to make adjustments to the inventory.

### Main Manager Menu
- **View Overall Sales**: Displays the total sales for the day.
- **Manage High-Level Operations**: Includes functionalities for managing overall store operations and high-level decision-making.

## Error Handling
The application includes comprehensive error handling to manage invalid inputs and unexpected issues gracefully. Users will receive appropriate messages guiding them on the correct usage of the application.

## File Handling
Data persistence is managed through the use of JSON files stored in the `data/` directory. This ensures that all information is saved and can be loaded when the application is restarted.

## Conclusion
This Supermarket application provides a robust simulation of a real-world supermarket system, demonstrating key object-oriented programming principles and practical functionalities. Enjoy using the application, and feel free to explore the various features available to different roles within the system.

---
