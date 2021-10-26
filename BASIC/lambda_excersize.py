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
    choice='yes'
    name=student['name']
    grades=student['grades']
    print(f"{name}:")

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
    