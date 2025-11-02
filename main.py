from classes.bank_account import BankAccount

b1 = BankAccount("hagay",100)

b2 = BankAccount("jacob",100)
print(b1.__str__())
print(b2.__str__())


b1.transfer_funds(b2,90)

print(b1.__str__())
print(b2.__str__())