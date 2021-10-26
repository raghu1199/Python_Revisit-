class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        a=self.m1+other.m1
        b=self.m2+other.m2
        obj=student(a,b)

        return (obj.m1,obj.m2)
    
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
    def __str__(self):
        return "{},{}".format(self.m1,self.m2)
        

s1=student(20,30)
s2=student(50,70)
s3=s1+s2
print(s3)

if s1>s2:
    print("S1 wins")
else:
    print("s2 wins")

#print(s1) prints object of class an address 
# overload __str__ to print vlues
print(s1)
print(s2)