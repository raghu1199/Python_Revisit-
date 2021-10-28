
class BankAccount:

    def __init__(self,name,acc_num,balance=0):
        self.transactions=[]
        self.name=name
        self.acc_num=acc_num
        self.balance=balance

class Account:
    li=[]
    def create_acc(self,name,acc_num,balance=0):
        self.acc=BankAccount(name,acc_num,balance)
        Account.li.append(self.acc)

    def deposite(self,amt):
        self.acc.balance+=amt
        self.acc.transactions.append(+amt)
        print(f"{amt} is deposited into {self.acc.name}")
    
    def withdrawl(self,amt):
        self.acc.balance-=amt
        self.acc.transactions.append(-amt)
        print(f"{amt} is withdrawl from {self.acc.name}")
    
    def recent_transactions(self):
        print("Recent transcaion is:",self.acc.transactions)

    @staticmethod
    def account_list():
        for acc in Account.li:
            print(acc.name,acc.acc_num,acc.balance)
    
    @staticmethod
    def manage_account():
        for acc in Account.li:
            if acc.balance<500:
                print("Warning ",acc.name ," is removed due to low balance")
                Account.li.remove(acc)

a=Account()
a.create_acc("Raghu",160130117047)
a.deposite(4000)
a.deposite(8000)
a.withdrawl(5000)
a.recent_transactions()
b=Account()
b.create_acc("Rahul",160130117040)
b.deposite(2000)
b.deposite(4000)
b.withdrawl(3000)
b.recent_transactions()
Account.account_list()
b.withdrawl(2600)
Account.manage_account()
Account.account_list()




