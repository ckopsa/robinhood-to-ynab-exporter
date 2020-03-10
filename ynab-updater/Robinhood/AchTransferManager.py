class AchTransferManager:
    def __init__(self, http_requester):
        self.requester = http_requester
        pass

    def get(self):
        url = "https://api.robinhood.com/ach/transfers/"
        response = self.requester.make_request(url)
        return [self.response_to_csv(result) for result in response["results"]]

    @staticmethod
    def response_to_csv(response):
        try:
            amount = response["amount"]
            direction = response["direction"]
            if direction == "withdraw":
                amount = "-" + amount
            merchant_category = response["direction"]
            merchant_description = "Deposit from Other Account"
            initiated_at = response["created_at"].split("T")[0]
            return amount, merchant_category, merchant_description, initiated_at
        except:
            pass