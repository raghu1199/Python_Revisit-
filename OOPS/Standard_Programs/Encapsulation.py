class car:
    __maxspeed=0
    __name=""

    def __init__(self):
        self.__maxspeed=200
        self.__name="Supercar"
        self.__updateSoft()
    
    def drive(self):
        print(f"{self.__name} driving at maxspeed {self.__maxspeed} ")
    
    def __updateSoft(self):
        print(f"updating soft on {self.__name} ")
    
    def setAttribute(self,maxspeed,name):
        self.__maxspeed=maxspeed
        self.__name=name
    def getAttribute(self):
        return self.__name,self.__maxspeed

redcar=car()
redcar.drive()
redcar.setAttribute(250,"Jaguar")
name,speed=redcar.getAttribute()
print(name,speed)
#redcar.__car1__updatesoft()