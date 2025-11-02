class BankAccount:
    def __init__(self, account_holder:str, initial_balance:float):
        self.holder = account_holder
        self.balance = initial_balance


    def transfer_funds(self,other_account, amount):
        if self.balance > amount:
            self.balance -= amount
            other_account.balance += amount
            print(f"{self.balance} the transfer are succes ")
        else:
            print("your have not enough money")

    def __str__(self):
        return f"the owner is: {self.holder} the balance is:{self.balance}"

