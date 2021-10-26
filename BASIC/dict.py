freinds={"rahul":23,"raghu":22,"ashu":24}
print(freinds["raghu"])

freinds["bob"]=26
freinds["raghu"]=21
print(freinds)

freinds=[{'name':"raghu","age":22},
  {'name':"rahul","age":22},
  {'name':"ashu","age":21},]

print(freinds[1]["name"])

for d in freinds:
    print(d['name'])

freinds1=[('rolf',24),('bob',30)]
f=dict(freinds1)
print(f)

for d in freinds:
    print(d['name']," ",d['age'])
    
f1={"name":"ADdskk",'age':204}
print(f1)
f1.update({"name":"abhb",'age':20})
print(f1)

my_freinds={
    '1':"raghu",
    '2':"ashu",
    '3':"ronak",
    '4':'abdja'
}

for id,name in my_freinds.items():
    print(id ," ",name)

grades=[80,75,90,200]
total=sum(grades)
length=len(grades)
average=total/length
print(total," ",average)

string="hello i ehee"
freq={}
for ch in string:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

print(freq)
