a=5
b=int(input("ENter num b:"))

# print(a/b) # b=0 gives zerodivision error below stmt now not executes

# print("Bye")

try:
    print(a/b)
except Exception as e:
    print("You can not divide by zero")

print("Bye")


