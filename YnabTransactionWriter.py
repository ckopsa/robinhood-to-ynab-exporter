from typing import List

import openapi_client
from openapi_client import Account, SaveTransaction, ApiException, SaveTransactionsWrapper

from TransactionBase import TransactionBase


class YnabTransactionWriter:
    @staticmethod
    def create(token):
        configuration = openapi_client.Configuration()
        configuration.api_key['Authorization'] = token
        configuration.api_key_prefix['Authorization'] = 'Bearer'
        configuration.host = "https://api.youneedabudget.com/v1"
        return YnabTransactionWriter(configuration)

    def __init__(self, configuration):
        self.configuration = configuration

    def write(self, transactions: List[TransactionBase]):
        with openapi_client.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            transaction_api = openapi_client.TransactionsApi(api_client)
            account_api = openapi_client.AccountsApi(api_client)
            try:
                accounts = account_api.get_accounts("last-used")
                accounts = accounts.data.accounts
                account: Account = list(filter(lambda account: account.name == 'Robinhood Unlinked', accounts))[0]
                transactions = [
                    SaveTransaction(account_id=account.id,
                                    date=transaction.transaction_date.isoformat(),
                                    amount=transaction.amount,
                                    memo=transaction.category,
                                    payee_name=transaction.payee) for transaction in transactions]
                data = SaveTransactionsWrapper(transactions=transactions)
                transaction_api.create_transaction('last-used', data)

            except ApiException as e:
                print("Exception when calling AccountsApi->get_account_by_id: %s\n" % e)
