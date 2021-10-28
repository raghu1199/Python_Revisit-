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

p1=Person("Raghu")
p2=Person("Rahul")
res=p1.compare(p2)
print(res)
p2.update(35)
res=p1.compare(p2)
print(res)