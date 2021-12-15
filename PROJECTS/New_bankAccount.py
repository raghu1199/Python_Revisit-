
class Account:
    li=[]
    
    
    

# increment class varibale by class name and then assign to object varibale so now each object get 
# unique value of class 

class BankAccount():
    ac_no=1000
    li=[]
    def __init__(self,name=None,pin=None,status=None,balance=0):
        if name!=None and pin!=None and status!=None:
            BankAccount.ac_no+=1  # update the class variable in each object creation
                
        self.acc_num=BankAccount.ac_no    # assign class var to object variable
        self.name=name
        self.pin=pin
        self.balance=balance
        self.status=status
        self.transactions=[]

    def create_acc(self,name,pin,status="inactive",balance=0):
        self.acc=BankAccount(name,pin,status,balance)  #customer bankaccount ojecs
        BankAccount.li.append(self.acc)
        print(f"Your account no is:{self.acc_num}") # it will give a=BankAccount() based acc num which 
        # was not incremented bt we have to ive self.acc object based accn no
        print(f"You acc no is:{self.acc.acc_num}")

    def deposit(self):
        #user_acc=input("enter account num:")
        # you will have bankacc object from for loop so direct use self.balanace here(acc.balance) instead of self.acc.balance
        # acc object dont have attrib self.acc 
        amt=int(input("Enter amount to deposite:"))
        self.balance+=amt
        self.transactions.append(f"+{amt}")
        if self.balance>=500:
            self.status="active"
        else:
            self.status="inactive"
        
        
    
    def withdraw(self):
        amt=int(input("Enter amount to withdraw:"))

        if self.balance>=500:
            if (self.balance-amt )>20:
                self.balance-=amt
                self.transactions.append(f"-{amt}")
                print(f"{amt} is withdrawn from {self.name} account")
            else:
                print("Can't Withdraw minimum balance reaches after withdraw(20 Rupee) .Try less amount")

        if self.balance<500:
            if (self.balance-amt)>20:
                print("Your balance is already below minimum balance. If u withdraw you will be charged penalty")
                choice=input("Do you want to continue?(y/n)")
                if choice=='y':
                    self.balance-=(amt+20)
                    self.transactions.append(f"-{amt}")
                    self.transactions.append(f"{-20}")
                    print(f"{amt} is withdrawn from {self.name} account")
                else:
                    print("Ok")

    def recent_transactions(self):
        print("Your recent transactions are:",self.transactions)
    
    def check_balance(self):
        print(f"Your current balance is:{self.balance}")
    
    def account_close(self):
        a_num=input("Enter account number:")
        for acc in BankAccount.li:
            if acc.acc_num==a_num:
                print(f"Account :{acc.name,acc.num} is closed.")
                BankAccount.li.remove(acc)
    



def menu():

    acounts=BankAccount.li
    ch=input("a:Already have an account \t n:Create a New Account\t q:Quit \n ")
    while ch!='q':
        if ch=='a':
            a_num=int(input("Enter account number:"))

            for acc in acounts:
                if acc.acc_num==a_num:
                    print("valid account")
                    print(f"Welcome {acc.name} in Our Banking system")
                    print()
                    user_pin=input("Enter your security Pin to make transactions:")
                    if acc.pin==user_pin:
                        choice=input("d:Deposite\t w:Withdraw\t c:CheckBalance\t r:To view Recent Transactions\t e:exit\t Close Account\n")
                        while choice!='e':
                            if choice=='d':
                                acc.deposit()   # it will use self.deposit here self=this acc used
                            elif choice=='w':
                                acc.withdraw()
                            elif choice=='c':
                                acc.check_balance()
                            elif choice=='r':
                                acc.recent_transactions()
                            elif choice=="l":
                                break
                            else:
                                print("invalid Choice please try again")

                            choice=input("d:Deposite\t w:Withdraw\t c:CheckBalance\t r:To view Recent Transactions\t e:exit\t Close Account\n")
                else:
                    print("Account Not exist Please Create new Account ")
        elif ch=='n':
            a=BankAccount()
            name=input("Enter Name:")
            pin=input("Enter your Security Pin(4 digit):")
            balance=int(input("Enter Amount to be deposited:(>500)"))
            if balance<500:
                print("Minimum Amount to be deposited is 500 at the time of creating Account")
                status="inactive"
                a.create_acc(name,pin,status,balance)
                print("Acount Created But Status is Inactive (You can't withdraw money)")
            else:
                status="active"
                a.create_acc(name,pin,status,balance)
                print("Acount Created And status is ACTIVE (You can withdraw money)")

        else:
            print("Invalid Choice")
        ch=input("a:Already have an account \t n:Create a New Account\t q:Quit \n ")



menu()


                
        

