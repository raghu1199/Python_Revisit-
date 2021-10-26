


freinds=['rolf','bob','anne']
family=['jen','charlie']

"""
usr_name=input("enter yr name:")

if usr_name in freinds:
    print("welcome freind")
elif usr_name in family:
    print("welcome family")
else:
    print("i dont know you")  

is_learning=True
while is_learning:
    print("You are learning..")
    u_input=input("Are you still learning?")
    is_learning=(u_input=='yes')
    print(is_learning)

print("end of learning")

is_running="yes"

while is_running=='yes':
    print("you are running..")
    is_running=input("Do you want continue?(yes/no)")
    
print("stopped running") """


# ask then if p the hello ,ask again
#if q then welcome ask again
# if e then terminate
"""
choice=input("enter ur choice\n(p->hello\nq->welcome\ne->exit\n")

while choice!='e':
    if choice=='p':
        print("HELLO\n")
    elif choice=='q':
        print('Welcome')
    choice=input("enter ur choice\n(p->hello\nq->welcome\ne->exit\n")  """

for i in range(0,20,2):
    print(i," ",end="")
fruits=['banana','orange','mango','apple']

for f in fruits:
    print(f)

print("c based")

for i in range(len(fruits)):
    print(fruits[i])

# else executed after termination of for loop ,
#if break executed then it goes out of for loop and else also
print()
numbers=[11,33,56,39]
for num in numbers:
    if num%2==0:
        print("list contains even numbers")
        break
else:
    print("list not conatin even numbers")

print("Your here after break")

students={'name':'Raghu','grade':90,'name2':'rahul','grade2':80}
for key,value in students.items():
    print(key," :",value)

cars=['ok','ok','ok','faulty','ok']
for status in cars:
    if status=='faulty':
        break
    print(f"car status is {status}")
for status in cars:
    if status=='faulty':
        print(f"cars is {status} so goes to next")
        continue
    print(f"car is {status}")

i=0
while i<10:
    if i==5:
        continue
    i=i+1
    print(f"i:{i}")

"""
for i in range(10):
    if i==5:
        continue
    print(f"i:{i}")"""

"""
freinds1={'raghu':22,'rahul':20,'bob':24,'hi':21}
name=input("Enter name")

if name in freinds1:
    print(f"I know this person")

for i in range(1,100):
    print("i:",i)
    if i%3==0:
        print("Fizz")
        if i%5==0:
            print("Buzz")
    elif(i%5==0):
        print("Buzz")"""
    
cars=['ok','ok','ok','ok']

for status in cars:
    if status=='faulty':
        print("Fault found Stopping") 
        break
else:
    print("All is ok") 

# prime

for n in range(2,11):
    for i in range(2,n):
        if n%i==0:
            print(f"{n}:{i}*{n//i}")
            break;
    else:
        print(f"{n} is prime")


