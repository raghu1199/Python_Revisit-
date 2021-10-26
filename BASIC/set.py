s1={"ashu","ronak"}
s1.add("milan")
s1.add(10)
print(s1)
s1.update(("karan","vikas"))
print(s1)
s1.remove("ashu")
print(s1)
s1.update(("ronak","rahul"))
"""
print(s1)
s1.clear()
print(s1)
s1.add("raghu")
print(s1)
del s1
print(s1) """

cs={'dsa','math','physics','history'}
art={'history','design','math'}
print(cs.intersection(art)) # common in both

print(cs.difference(art)) # present in cs but not in art
print(art.difference(cs)) # present in art bt not in cs

print(cs.symmetric_difference(art))
if 'dsa' in art:
    print("yes")
else:
    print("No")

t=(15)
print(type(t))
t=(15,)
print(type(t))
t=15,16
print(t,"type:",type(t))