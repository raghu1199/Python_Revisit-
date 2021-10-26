
#method overload Not supported in pyhton
# method overload > same method name with different signature
# with diff no of args
def sum(a=None,b=None,c=None):
   s=0
   if a!=None and b!=None and c!=None:
      s=a+b+c
   elif a!=None and b!=None:
      s=a+b
   else:
      s=a
   
   print(s)

sum(1,2,3)
sum(1,2)
sum(1)
# method override if subcalss and superclass have 
# same method name with same signature 
# then sublcass method will override superclass method
class college:
   def exam(self):
      print("Exam was held by college")

class student(college):
   def exam(self):
      print("Exam given by student..")

s=student()
s.exam()





