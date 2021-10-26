class Student:
    college="NIT"
    count=0
    def __init__(self,name,ma1,ma2,ma3):
        self.name=name
        self.m1=ma1
        self.m2=ma2
        self.m3=ma3
        Student.count+=1
    
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    # intance method ,can access class var,instance var
    def info(self):
        print(f"{self.name} {self.college} ")  
    
    @classmethod
    def getCollege(cls):
        print(f"college name:{cls.college} students:{cls.count}")

    @staticmethod
    def info_college():
        print("This is NIT-Hamirpur college")


st1=Student("Raghu",89,90,93)
st2=Student("Rahul",90,91,93)
print(st1.avg())
st1.info()
st1.getCollege()
Student.getCollege()
Student.info_college()