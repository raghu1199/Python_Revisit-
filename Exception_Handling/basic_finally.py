#if error occures , below this stmt nothing excutes it will excutes except block
#so resorce still unclosed if we put close in except then
# if no error occures except not executed so still not closed
# a=5
# b=int(input("Enter inum b:"))

# try:
#     print("resorce open")
#     print(a/b)
#     print("resource closed")
# except Exception as e:
#     print("Cant divide by zero")

# print("Bye")

from typing import final


# finally alwalys excuted irrespective of error occurance
a=5
b=int(input("Enter inum b:"))

try:
    print("resorce open")
    print(a/b)

except Exception as e:
    print("Cant divide by zero")
finally:
    print("resource closed")

print("Bye")