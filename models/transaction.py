class Transaction:
    def __init__(self, transaction_id, product_id, quantity, transaction_type, date):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.quantity = quantity
        self.transaction_type = transaction_type  # 'buy' or 'sell'
        self.date = date

    def __repr__(self):
        return f"Transaction({self.transaction_id}, {self.product_id}, {self.quantity}, {self.transaction_type}, {self.date})"