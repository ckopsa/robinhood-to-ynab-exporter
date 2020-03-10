class TransactionManager:
    def __init__(self, http_requester):
        self.requester = http_requester
        pass

    def get(self):
        return [self.response_to_csv(transaction) for transaction in
                self.get_pending_transactions() + self.get_settled_transactions()]

    def get_pending_transactions(self):
        card_endpoint = "https://minerva.robinhood.com/cards/pending_transactions/"
        transaction_endpoint = "https://minerva.robinhood.com/history/pending_transactions/"
        return self.get_transactions_helper(transaction_endpoint, card_endpoint)

    def get_settled_transactions(self):
        transaction_endpoint = "https://minerva.robinhood.com/history/settled_transactions/"
        card_endpoint = "https://minerva.robinhood.com/cards/settled_transactions/"
        return self.get_transactions_helper(transaction_endpoint, card_endpoint)

    def get_transactions_helper(self, transaction_endpoint, card_endpoint):
        response = self.requester.make_request(transaction_endpoint)
        source_ids = [result["source_id"] for result in response["results"]]
        return [self.requester.make_request(card_endpoint + source_id + "/") for source_id in source_ids]

    @staticmethod
    def response_to_csv(response):
        try:
            amount = response["amount"]["amount"]
            direction = response["direction"]
            if direction == "debit":
                amount = "-" + amount
            merchant_category = response["merchant_category"]
            merchant_description = response["merchant_description"]
            initiated_at = response["initiated_at"].split("T")[0]
            return amount, merchant_category, merchant_description, initiated_at
        except:
            pass
