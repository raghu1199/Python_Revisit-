class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"{self.name} {self.age}")
    
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
    
    

p1=Person("Ritesh",23)
p1.show()
p2=Person("Raghu",24)

if p1.compare(p2):
    print("Both equal")
else:
    print("Not equal")


