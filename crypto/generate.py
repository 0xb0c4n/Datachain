from eth_account import Account
import secrets

class Generate:
    def __init__(self):
        self.private_key = secrets.token_hex(32)
        self.acct = Account.from_key(self.private_key).address

    def get(self):
        return self.private_key, self.acct        