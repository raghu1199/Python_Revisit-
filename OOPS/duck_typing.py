# class must have method implemtation so that irrespective
# of type of object it should execute that specific method 

class Pycharm:
    def execute(self):
        print("compiling")
        print("Running")

class VisualStudio:
    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("compiling")
        print("Running")

class laptop:
    def code(self,ide):
        ide.execute()

ide1=Pycharm()
ide2=VisualStudio()

lap=laptop()
lap.code(ide1)
print()
lap.code(ide2)