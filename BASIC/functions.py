"""
def greet():
    name=input("Enter your name:")
    print(f"Welcome {name}")

greet() "

# variable scope
x="global x"
def test():
    y="local y"
    x="local x"
    print(y,":","x:",x)

test() 

# access global var inside func
x='global x'
print(id(x))

def test():
    global x
    print(x," id:",id(x))

test() 

def test():
    global x
    x=5
    print("inside func:",x)

test()
print("x:",x)
x=6
test()

prev=10
for i in range(5,20):
    if i>prev:
        prev=i

print(prev)

def outer():
    x='outer'
    def inner():
        x='inner'
        print("inside inner:",x)
    
    inner()
    print("inside outer:",x)

outer() """

def outer():
    x='outer'
    def inner():
        print("inside inner:",x)
    
    inner()
    print("inside outer:",x)
    
outer()
details={"maker":'ford','mileage':2300,'fuel':460}
print(details)

def calculate(detail):
    mpg=detail['mileage']/detail['fuel']
    name=detail['maker']
    print(f"{name} gives {mpg} miles per gallon.")

calculate(details)

cars=[{"maker":'ford','mileage':2300,'fuel':460},
    {"maker":'tata','mileage':2400,'fuel':560},
    {"maker":'maruti','mileage':2600,'fuel':360},
]

print()
for car in cars:
    calculate(car)

print()
for i in range(len(cars)):
    calculate(cars[i])

# function return based
print()
def calculate_mpg(car):
    mpg=car['mileage']/car['fuel']
    return mpg

def car_name(car):
    name=car['maker']
    return name
def print_car_info(car):
    name=car_name(car)
    mpg=calculate_mpg(car)
    print(f"{name} gives {mpg} miles per gallon new function" )

for car in cars:
    print_car_info(car)

def devide(x,y):
    if y==0:
        return "you tried to devide by zero"
    else:
        return x/y

print(devide(10,2))
print(devide(10,0))

def add(x,y=5):
    return x+y

print(add(6))  # takes default parameter value
print(add(6,10))



