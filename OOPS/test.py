class Student:
    def __init__(self,name):
        self.name=name
    
class College:
    def __init__(self,students=[]):
        self.students=students
    def show(self,obj):
        print(obj.name)

s1=Student("Raghu")
s2=Student("Rahul")
c=College([s1,s2])
c.show(s1)

