Product Management System

This is a simple product management system implemented in Python. It allows you to add, update, and manage products, as well as track available stock and handle sales.

Features

Add Product: Add a new product to the catalog.
Update Price: Update the price of an existing product.
Update Quantity: Update the quantity of an existing product.
Sell Product: Sell a specified quantity of a product.
Available Stock: View all available products and their details.

Class Structure

 `Product`

The `Product` class manages individual products and maintains a catalog of all products.

#### Attributes

- `product_id`: Unique identifier for the product.
- `product_name`: Name of the product.
- `product_description`: Description of the product.
- `product_price`: Price of the product.
- `product_quantity`: Quantity of the product available in stock.
- `online_products`: Class dictionary to store all products.

Methods

- `__init__(self, product_id, product_name, product_description, product_price, product_quantity)`: Initializes a new product and adds it to the catalog.
- `add_product(self)`: Prompts user input to add a new product.
- `update_price(self, new_price)`: Updates the price of the product.
- `update_quantity(self, new_quantity)`: Updates the quantity of the product.
- `sell(self, quantity_sold)`: Sells a specified quantity of the product.
- `available_stock(cls)`: Class method to display all available products and their details.
- `start(cls)`: Class method to start the interactive menu for managing products.

 Getting Started

To get started with this project, clone the repository and run the script.

 Prerequisites

- Python 3.x

Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/product-management-system.git
    ```

2. Navigate to the project directory:
    ```sh
    cd product-management-system
    ```

3. Run the script:
    ```sh
    python product_management.py
    ```

Usage

When you run the script, you will see a menu with the following options:

1. Available stock: View all products in the catalog.
2. Update price: Update the price of an existing product.
3. Update quantity: Update the quantity of an existing product.
4. Purchase: Sell a specified quantity of a product.
5. Add new product: Add a new product to the catalog.
6. Exit: Exit the program.

Follow the prompts to manage the products in your catalog.

Example

An initial product is created for demonstration purposes:

- Product ID: `12345`
- Product Name: `Toyota Yaris`
- Description: `Fairly used car`
- Price: `$1500.00`
- Quantity: `10`

Run the script and use the menu to interact with this product and add new ones.



