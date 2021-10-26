# abstract class, method not supported deafult in pyhton
from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    #pass
    def process(self):
        print("Its Running")

#c=Computer() # Abstract class can't be instantiated
#l=Laptop() # if sublcass not implemented all of abstract 
    #method of abstract class then you cant create object of subclass

l=Laptop()
l.process()