from HttpRequester import HttpRequester
from TransactionManager import TransactionManager
from TransferManager import TransferManager
from AchTransferManager import AchTransferManager


class RobinhoodTransactionSupplier:
    @staticmethod
    def create(auth_token):
        http_requester = HttpRequester(auth_token)
        return RobinhoodTransactionSupplier(
            transferManager=TransferManager(http_requester),
            transactionManager=TransactionManager(http_requester),
            achTransferManager=AchTransferManager(http_requester)
        )

    def __init__(self, transferManager, transactionManager, achTransferManager):
        self.transferManager = transferManager
        self.transactionManager = transactionManager
        self.achTransferManager = achTransferManager

    def get(self):
        return self.transferManager.get() + self.transactionManager.get() + self.achTransferManager.get()
