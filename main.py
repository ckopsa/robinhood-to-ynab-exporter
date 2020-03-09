from __future__ import print_function

from datetime import date

from RobinhoodTransactionSupplier import RobinhoodTransactionSupplier
from TransactionBase import TransactionBase
from YnabTransactionWriter import YnabTransactionWriter
from credentials import robinhood_token, ynab_token

rbh_transaction_supplier = RobinhoodTransactionSupplier.create(robinhood_token)

ynab_transaction_writer = YnabTransactionWriter.create(ynab_token)

transactions = rbh_transaction_supplier.get()
transactions = filter(lambda x: x is not None, transactions)

transactions = [TransactionBase(int(float(transaction[0]) * 1000), date.fromisoformat(transaction[3]), transaction[2],
                                transaction[1]) for
                transaction in
                transactions]

last_transaction_date: date = date.fromisoformat('2020-02-20')
transactions: [TransactionBase] = list(filter(lambda x: x.transaction_date > last_transaction_date, transactions))
print("Writing the following transactions:")
for transaction in transactions:
    print(transaction.payee, transaction.amount, transaction.category, transaction.transaction_date)
if input("Are you sure you want to continue? (Y\\n): ") == 'Y':
    ynab_transaction_writer.write(transactions)
