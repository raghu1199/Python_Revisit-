class Employee:
    raise_amt=1.03

    @classmethod
    def set_raise(cls,amt):
        cls.raise_amt=amt
    
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    
    def apply_raise(self):
        self.pay=self.pay*self.raise_amt

    def info(self):
        print(self.name,self.raise_amt,self.pay)

e1=Employee("Raghu",50000)
e2=Employee("Rahul",60000)
e1.raise_amt=1.7
e2.raise_amt=1.5
e1.apply_raise()
e2.apply_raise()
e1.info()
e2.info()
print("After class raise")
Employee.set_raise(1.6)
e1.info()
e2.info()


