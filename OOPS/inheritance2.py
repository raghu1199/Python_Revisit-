class Student:
    def __init__(self,name,marks=None):
        self.name=name
        if marks is None:
            marks=[]
        else:
            self.marks=marks
    def average(self):
        return sum(self.marks)/len(self.marks)

    def show(self):
        print(f"{self.name} {self.marks} {self.average()}")

class WorkingStudent(Student):
    def __init__(self,name,marks=None,salary=8000):
        super().__init__(name,marks)
        self.salary=salary
    
    def weekly_salary(self):
        return self.salary/4
    
    def show(self):
        super().show()
        print("salary is:",self.salary," weekly salary is:",self.weekly_salary())
    

raghu=Student("raghu",[89,90,93,95])
rahul=WorkingStudent("rahul",[80,87,83,89],16000)
raghu.show()
rahul.show()


    
