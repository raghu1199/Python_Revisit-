class B:
    def f(self):
        print("Inside B")
class C:
    def f(self):
        print("Inside C")

    def f2(self):
        print("Inside c twice")

class D(B,C):
    def f(self):
        super().f()
        C.f(self)
        print("Inside D")
    
d=D()
d.f()
#d.f2()

class A:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @property
    def weekly_salaray(self):
        return self.salary*500

raghu=A("Ragu",100)
print(raghu.weekly_salaray)



