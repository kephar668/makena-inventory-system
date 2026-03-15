class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product({self.product_id}, '{self.name}', {self.price}, {self.quantity})"

    def update_quantity(self, amount):
        self.quantity += amount

    def update_price(self, new_price):
        self.price = new_price