class Employee:
    raise_amt=1.03
    no_of_emps=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        self.email=name+'@gmail.com'
        Employee.no_of_emps+=1
        
    def apply_raise(self):
        self.salary=int(self.salary*self.raise_amt)

    @classmethod
    def set_raise(cls,amt):
        cls.raise_amt=amt

    def display_emp(self):
        print(f"name:{self.name} email:{self.email} salary:{self.salary} raise:{self.raise_amt} ")

class Devloper(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language=language

    def display_emp(self):
        super().display_emp()
        print("prog language:",self.language)

class Manager(Employee):
    def __init__(self,name,salary,employees=None):
        super().__init__(name,salary)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        print("Employees under this manager:")
        for emp in self.employees:
            emp.display_emp()

d1=Devloper("raghu",50000,"Python")
d2=Devloper("Rahul",40000,"C")
e1=Employee("Ashu",45000)
Employee.raise_amt=4.5
d1.apply_raise()
#d1.display_emp()

e1.apply_raise()
mgr=Manager("Raghu",90000)
mgr.add_emp(e1)
mgr.add_emp(d1)
mgr.add_emp(d2)
mgr.print_emps()

Employee.set_raise(2.7)
print("After rasie")
mgr.print_emps()
print("Total:",Employee.no_of_emps)
print(Employee.raise_amt)


