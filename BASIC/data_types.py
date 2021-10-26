freinds=["Raghu","Rahul","Ashu","asasd"]
print(len(freinds)," ",freinds[1])
freinds.append("abhijit")
freinds.append("mukul")
print(len(freinds),freinds[4])

ff=[["Raghu",22],["Rahul",23],["Ashu",23]]
print(ff[1])
print(ff[1][0]," ",ff[2][1])

for f in ff:
    print(f[0])

for i in range(len(ff)):
    print(ff[i])

freinds.remove("Rahul")
print(freinds)
freinds.insert(3,"Ronak")
print(freinds)
new=['abhijit1','mukul1']
freinds.extend(new)
print(freinds)
print('milan' in freinds)
for index,item in enumerate(freinds):
    print(index,item)

nums=[1,5,4,2,3]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# do not alter original
not_alter=sorted(nums)
print(not_alter)
print("original:",nums)
print("min:",min(nums),"max:",max(nums),"sum:",sum(nums))
print(nums.index(3))



# convert list into strings
print(type(freinds))
fstr=",".join(freinds)
print(fstr," ",type(fstr))

# convert string to list
f_list=fstr.split(',')
print(f_list," ",type(f_list))



