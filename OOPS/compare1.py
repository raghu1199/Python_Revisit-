class Person:
    def __init__(self,name):
        self.name=name
        self.age=18

    def update(self,age):
        self.age=age
    
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

p1=Person("raghu")
p2=Person("Rahul")

print(p1.compare(p2))
p2.update(30)

print(p2.compare(p1))