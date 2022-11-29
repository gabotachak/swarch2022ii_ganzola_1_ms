class ForbiddenException(Exception):
    def __init__(self, message):
        self.message = message


class InsufficientFundsException(ForbiddenException):
    def __init__(self, user=None):
        self.message = f"{user} has insufficient funds to complete the transaction."
