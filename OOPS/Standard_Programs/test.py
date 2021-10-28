#1)
l=['y','y','y','n','y','n']
for i in range(len(l)):
    if l[i]=='n':
        print(i)

class Garage:
    def __init__(self,car):
        self.cars=car
    
    def __len__(self):
        return len(self.cars)

    def __getitem__(self,i):
        return self.cars[i]
    def __str__(self):
        return f"garage with {len(self.cars)} cars"
    
    def __repr__(self):
        return f"<Garage {self.cars} "

ford=Garage(['Fiesta','Fiesta1','Fiesta3','Focus'])
print(len(ford))
print(ford[0])
for car in ford:
    print(car)

print(ford)
print(ford.__repr__())
