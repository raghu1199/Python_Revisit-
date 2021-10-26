class Employee:
    raise_amt=1.04
    count=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.count+=1
    
    def info(self):
        return "{} {}".format(self.name,self.salary)
    
    def apply_raise(self):
        self.salary=int(self.salary*self.raise_amt)
        print(f"{self.salary} raise_amt:{self.raise_amt}")
    

emp1=Employee('RAghu',50000)
emp2=Employee('Abhijit',60000)

print(emp1.__dict__)
print(Employee.__dict__)
emp1.raise_amt=1.06
print(emp1.__dict__)

emp1.apply_raise()
emp2.apply_raise()
print(emp1.info())
print(emp2.info())
print(Employee.info(emp1))