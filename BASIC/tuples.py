t1=('history','physics')
t2=t1
print(t2)
l=[5,4,3]
t=('raghu',l)
print(t)
t[1][0]=8
print(t)
l.append(10)
print(t)
newt=t1+('raghu','rahul')
print(newt)

t2=(0,1,2,3,4)
print(max(t2)," ",min(t2))
t1=('raghu','python')
t2=('raghu','python')
res=(t1>t2)-(t1<t2)
print(res)
for i in t1:
    print(i)

tup=(0,1,2,3,4)
print(tup[:4])
li=[0,1,2,3,4,5,6,7,8,9,10,11]
print(li[10:2:-2])
for index,item in enumerate(tup):
    print(index,item)

a={"x":100,"y":200}
b=list(a.items())
print(b)
print(a.items())




