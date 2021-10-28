class Duck:
    def quack(self):
        print("quack")
    def fly(self):
        print("Fly")

class Person:
    def quack(self):
        print("quacking like duck")
    def fly(self):
        print("Flying like duck")

def q_and_f(object):
    if isinstance(object,Duck):
        object.quack()
        object.fly()
    else:
        print("Object has to be Duck only")

def q_and_f1(obj):
    try:
        obj.quack()
        obj.fly()
        obj.bark()
    except AttributeError as e:
        print(e)

d=Duck()
p=Person()
q_and_f(d)
q_and_f(p)
q_and_f1(p)
q_and_f1(p)