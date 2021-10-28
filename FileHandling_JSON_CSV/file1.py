 # read and write file with help of context-manager
# with open("File_handling/test.txt","r") as f:
#     print(f.readline(),end="")
#     print(f.readline())

# read large file with for loop
# with open("File_handling/test.txt","r") as f:
#     print(f.read(7),end="*")
#     for line in f:
#         print(line,end="")

# read whole file with each time 10 char 
# with open("File_handling/test.txt","r") as f:
#     f_contents=f.read(10)
#     while len(f_contents)>0:
#         print(f_contents,f.tell(),end="*")
#         f_contents=f.read(10)

# with help of seek(pos)
# with open("File_handling/test.txt","r") as f:
#     f_contents=f.read(20)
#     print(f_contents)
#     print(f.tell())
#     f.seek(10)
#     print(f.tell())
#     print(f.read(10))
#     print(f.tell())
# Write into file
# with open("File_handling/test1.txt","a") as f:
#     f.write("555ELCOME RAGHU\nHOW ARE YOU")
#     f.write("55HELLO RAHUL")

# read file1 and write its content to (copy) another file
with open("File_handling/test.txt","r") as rf:
    with open("File_handling/test1.txt","w") as wf:
        for line in rf:
            wf.write(line)

