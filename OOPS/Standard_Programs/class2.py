class Computer:
    count=0
    def __init__(self,cpu,ram,brand):
        self.cpu=cpu
        self.ram=ram
        self.brand=brand
        Computer.count+=1
    
    def config(self):
        print(f"{self.cpu} {self.ram} {self.brand} ")

com1=Computer("i3","4GB","Dell")
com2=Computer("i5","8GB","Lenovo")
com3=Computer("i7","8GB","Hp")
com1.config()
com2.config()
com3.config()
print(Computer.count)