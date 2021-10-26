class student:
    def __init__(self,name,roll,brand,ram,cpu):
        self.name=name
        self.roll=roll
        self.lap=self.laptop(brand,ram,cpu)

    
    def show(self):
        print(f"{self.name} {self.roll}")
        self.lap.show()
    
    class laptop:
        def __init__(self,brand,ram,cpu):
            self.brand=brand
            self.ram=ram
            self.cpu=cpu
        def show(self):
            print(f"{self.brand} {self.ram} {self.cpu}")



#lap=student.laptop()
#lap.show()

s=student("raghu","21mcs022","Lenovo",18,"i9")
s.show()