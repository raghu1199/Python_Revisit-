class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def from_String(cls,emp_string):
        name,salary=emp_string.split("-")
        return cls(name,salary)
    
    def info(self):
        print(f"name:{self.name} salary:{self.salary}")
    
obj=Employee.from_String("Raghu-50000")
obj.info()
