class Product:
    online_products = {}

    def __init__(self, product_id, product_name, product_description, product_price, product_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_quantity = product_quantity
        Product.online_products[product_id] = self

    def add_product(self):
        product_id = input("Enter the product ID: ")
        if product_id in Product.online_products:
            print("Product is already in the catalog.")
            return
        
        product_name = input("Enter the product name: ")
        product_description = input("Enter the product description: ")
        product_price = float(input("Enter the product price: "))
        product_quantity = int(input("Enter the product quantity: "))

        Product(product_id, product_name, product_description, product_price, product_quantity)
        print("Product added successfully.")

    def update_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.product_price = new_price

    def update_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.product_quantity += new_quantity

    def sell(self, quantity_sold):
        if quantity_sold < 0:
            raise ValueError("Quantity sold cannot be negative")
        if quantity_sold > self.product_quantity:
            raise ValueError("Not enough goods available")
        self.product_quantity -= quantity_sold

    @classmethod
    def available_stock(cls):
        if not cls.online_products:
            return "No products available."
        stock_info = []
        for product_id, product in cls.online_products.items():
            stock_info.append(
                f"Product ID: {product.product_id}, Name: {product.product_name}, "
                f"Description: {product.product_description}, Price: ${product.product_price:.2f}, "
                f"Quantity available: {product.product_quantity}"
            )
        return "\n".join(stock_info)

    @classmethod
    def start(cls):
        while True:
            print("\n1. Available stock\n2. Update price\n3. Update quantity\n4. Purchase\n5. Add new product\n6. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                print(cls.available_stock())
            elif choice == "2":
                product_id = input("Enter the product ID to update the price: ")
                if product_id in cls.online_products:
                    new_price = float(input("Enter new price: "))
                    cls.online_products[product_id].update_price(new_price)
                    print("Price updated successfully.")
                else:
                    print("Product not found.")
            elif choice == "3":
                product_id = input("Enter the product ID to update the quantity: ")
                if product_id in cls.online_products:
                    new_quantity = int(input("Enter quantity to add: "))
                    cls.online_products[product_id].update_quantity(new_quantity)
                    print("Quantity updated successfully.")
                else:
                    print("Product not found.")
            elif choice == "4":
                product_id = input("Enter the product ID to purchase: ")
                if product_id in cls.online_products:
                    quantity_sold = int(input("Enter quantity to sell: "))
                    cls.online_products[product_id].sell(quantity_sold)
                    print("Sale completed successfully.")
                else:
                    print("Product not found.")
            elif choice == "5":
                cls.add_product(cls)
            elif choice == "6":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Initial product for demonstration
product = Product("12345", "Toyota Yaris", "Fairly used car", 1500.0, 10)
Product.start()
