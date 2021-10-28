stu=int(input("how many stu:"))
n=[]
t=[]
for i in range(stu):
    name=input("enter name of stu:")
    n.append(name)
    subj=int(input("enter how many subj:"))
    total=0
    for j in range(subj):
        sub_name=input(f"enter {j+1}sub name:")
        marks=int(input(f"enter {sub_name} marks:"))
        total=total+marks
    t.append(total)
    print(total)
print(n)
print(t)
