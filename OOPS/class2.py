class Computer:
    count=0
    def __init__(self,cpu,ram,brand):
        self.cpu=cpu
        self.ram=ram
        self.brand=brand
        Computer.count+=1
    
    def config(self):
        print(f"{self.cpu} {self.ram} {self.brand}")
    

c1=Computer('i3',8,'HP')
c2=Computer('i5',12,'dell')
c3=Computer('i9',6,'acer')
c1.config()
c2.config()
print(Computer.count)
