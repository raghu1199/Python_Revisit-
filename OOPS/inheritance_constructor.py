class A:
    def __init__(self):
        print("In A init")
    
class B(A):
    def __init__(self):
        #super().__init__()
        print("IN B Init")
    
#b=B()

class A1:
    def __init__(self):
        print("In A1")
    def feature1(self):
        print("In A1 feature1")
    
class B1:
    def __init__(self):
        print("In B1 init")

    def feature1(self):
        print("in B1 Feature1..")

    def feature2(self):
        print("In feature B1")

class C1(A1,B1):
    def __init__(self):
        super().__init__()
        print("in C1 init")

    def f(self):
        super().feature2()

c=C1()
c.feature1()
c.f()

    

