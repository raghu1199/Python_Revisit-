def greet():
    print("Hello")

hello=greet
hello()

# first class function-> you can pass function 
#to another func as arguments

def shout(text):
    return text.upper()

def greet(function):
    greeting=function("i am raghu")
    print(greeting)

greet(shout)

# function can return function 
def add1(x):
    def add2(y):
        return x+y
    return add2

add_num2=add1(20)
res=add_num2(30)
print(res)

def mul1(x):
    def mul2(y):
        return y*x

    return mul2

num2=mul1(10)
res=num2(15)
print(res)

def shout(text):
    return text.upper()

def low(text):
    return text.lower()

def greet(func,name):
    msg="welcome to india "+name
    greeting=func(msg)
    print(greeting)

greet(shout,"raghu")
greet(low,'RAGHU')