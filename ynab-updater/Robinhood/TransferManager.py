class TransferManager:
    def __init__(self, http_requester):
        self.requester = http_requester
        pass

    def get(self):
        url = "https://api.robinhood.com/ach/received/transfers/"
        response = self.requester.make_request(url)
        return [self.response_to_csv(result) for result in response["results"]]

    @staticmethod
    def response_to_csv(response):
        try:
            amount = response["amount"]["amount"]
            direction = response["direction"]
            if direction == "debit":
                amount = "-" + amount
            merchant_category = response["description"]
            merchant_description = response["originator_name"]
            initiated_at = response["initiated_at"].split("T")[0]
            return amount, merchant_category, merchant_description, initiated_at
        except:
            pass