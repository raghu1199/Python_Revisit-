f=['Rolf','Charlie','Anne','Bob','Jen']

# rolf:-5,charlie:-4,anne:-3,bob:-2,jen:-1

print(f[1:]) # charlie to end
print(f[:3]) #['Rolf', 'Charlie', 'Anne']

print(f[-2:]) #['Bob', 'Jen']
print(f[-1]) #last element jen
print(f[-1:4]) # last elemnt to 4th elemnt(from start) here nothing so []

print(f[-1:1:-1]) #['Jen', 'Bob', 'Anne'] last to first(1st index excluded) each time -1 gap
print(f[-1:2:-1]) # jen bob

print(f[-1:2]) # nothing ,no direction to go
print(f[-4:3:1]) # charlie to index 3(exclude) in gap of 1
