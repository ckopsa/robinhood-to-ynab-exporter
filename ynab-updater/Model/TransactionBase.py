from datetime import date
class TransactionBase:
    def __init__(self, amount, transaction_date: date, payee, category):
        self.amount = amount
        self.transaction_date: date = transaction_date
        self.payee = payee
        self.category = category