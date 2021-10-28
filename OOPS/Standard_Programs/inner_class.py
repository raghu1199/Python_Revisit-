class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.roll)
        self.lap.show()
    
    class laptop:
        def __init__(self):
            self.brand="Hp"
            self.cpu="i7"
            self.ram=8
        
        def show(self):
            print(self.brand,self.cpu,self.ram)
    
s1=student("raghu",47)
s2=student("rahul",40)
s1.show()
s2.show()
s1.lap.brand="Lenovo"
s1.lap.cpu='i5'
s2.lap.brand="Dell"
s2.lap.ram=4
print()
s1.show()
s2.show()