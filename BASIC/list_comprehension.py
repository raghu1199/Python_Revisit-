numbers=[1,2,3,4]
after=[]

for num in numbers:
    after.append(num*2)

print(after)

double_compre=[num*2 for num in numbers]
print(double_compre)
ages=[22,21,23,24,25]
age_string=[f"my freind is {age} years old" for age in ages]
print(age_string)

names=["ROLF","BOB","JEN"]
lower=[name.lower() for name in names]
print(lower)

"""
f=input("Enter your freind name:")
freinds=['Rahul','Ashu','Ronak','Abhijit']
freinds_lowered=[freind.lower() for freind in freinds]

if f.lower() in freinds_lowered:
    print(f"{f} is my freind")
else:
    print(f"{f} is not my freind")  """


ages=[22,35,36,27,21,20]

odd_ages=[age for age in ages if age%2==0]
print(odd_ages)

freinds=['Rahul','Ashu','Jayant','Vikas']
guests=['Ronak','Rahul','Vikas','Milan']

f_loweredSet=set([ name.lower() for name in freinds])
g_loweredSet=set([ name.lower() for name in guests ])

print(f_loweredSet.intersection(g_loweredSet))


present_freinds=[  guest.title() for guest in guests if guest.lower() in f_loweredSet]
print(present_freinds)


freinds=['Rahul','Vikas','Ashu','Abhijit','Mukul','Raghu']
grades=[80,78,82,89,92,93]

freind_grade={
    freinds[i]:grades[i] for i in range(len(freinds))
}

print(freind_grade)

freinds_grade={
    freinds[i]:grades[i] for i in range(len(freinds)) if grades[i]>90
}
print(freinds_grade)

grades1=list(zip(freinds,grades))
print("using zip:",grades1)



