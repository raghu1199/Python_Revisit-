from matplotlib import pyplot as plt

plt.plot([1,2,3],[2,5,7])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Raghu's Data")
plt.show()



data={'C':25,'C++':15,'Java':20,'Python':35}
courses=list(data.keys())
values=list(data.values())

fig=plt.figure(figsize=(10,5))
plt.bar(courses,values,color="maroon",width=0.4)
plt.xlabel("courses")
plt.ylabel("values")
plt.title("Student enrolled n courses")
plt.show()