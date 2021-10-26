class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def show(self):
        print(f"{self.name} {self.salary}")

class Developer(Employee):
    def __init__(self,name,salary,prog_lang):
        super().__init__(name,salary)
        self.prog_lang=prog_lang
    
    def show(self):
        return f"{self.name} {self.salary} {self.prog_lang}"
    

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
            print(f"{emp.name} ADDED SUCCES..")
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print(f"{emp.name} REMOVED SUCCESSFULLY..")

    def print_emps(self):
        for emp in self.employees:
            print("-->",emp.show())


d1=Developer("Raghu",50000,'python')
d2=Developer("Rahul",60000,"C++")
print(d1.name)

mgr=Manager("Raghvendra",70000,[d1])
mgr.print_emps()
mgr.add_emp(d2)
mgr.print_emps()
mgr.remove_emp(d2)
mgr.print_emps()


