a=5
b=int(input("Enter inum b:"))

try:
    print("resorce open")
    print(a/b) # gives zeroDivisionError
    k=int(input("Enter number not string k:"))
    print(k) # gives ValueError

except ZeroDivisionError as e:
    print("Cant divide by zero")
except ValueError as e:
    print("Please input int not string")
except Exception as e:
    print("Something went Wrong.. general exception")
finally:
    print("resource closed")

print("Bye")