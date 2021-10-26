def divide(x,y):
    return x/y

res=lambda x,y:x/y

print(divide(10,5))
print(res(20,5))

mul=lambda x,y,z:x*y*z

print(mul(2,4,5))

students=[
    {'name':'raghu','grades':{67,90,95,99}},
     {'name':'rahul','grades':{65,88,94,98}},
      {'name':'ashu','grades':{69,79,80,78}},
       {'name':'abhijit','grades':{50,90,95,76}}
]
def  average(grades):
    return sum(grades)/len(grades)

for student in students:
    grades=student['grades']
    avg=average(grades)
    name=student['name']
    print(f"{name} got average:{avg} marks")

avg=lambda grades:sum(grades)/len(grades)

for student in students:
    avg_marks=avg(student['grades'])
    print(f"{avg_marks} ")

# Imporatnt function down here

students=[
    {'name':'raghu','grades':{67,90,95,99}},
     {'name':'rahul','grades':{65,88,94,98}},
      {'name':'ashu','grades':{69,79,80,78}},
       {'name':'abhijit','grades':{50,90,95,76}}
]
operations={
    'average':lambda grades:sum(grades)/len(grades),
    'total':lambda grades:sum(grades),
    'max':lambda grades:max(grades)
}
choice="yes"
for student in students:
    name=student['name']
    grades=student['grades']
    print(f"{name}:")
    op=input("enter operation:avearge/total/max:")
    res=operations[op](grades)
    print(f"{op} is:{res}")

    choice=input("do you want more ops?(yes) or next?:")

    while choice!='next':
        op=input("enter operation:avearge/total/max:")
        if op in operations:
            res=operations[op](grades)
            print(f"{op} is:{res}")
        else:
            print("Wrong operation choosen.try again...")
            continue
        choice=input("do you want more ops or next?:")
        if choice=='next':
            break
    
        