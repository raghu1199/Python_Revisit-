class A:
    def feature1(self):
        print("f1")

class B(A):
    def feature2(self):
        print("feature2")

class C(B):
    def feature3(self):
        print("feature3")

obj=C()
obj.feature1()
obj.feature2()
obj.feature3()

b=B()
b.feature1()
b.feature2()