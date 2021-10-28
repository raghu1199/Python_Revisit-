class Animal:
    def breath(self):
        print("I breath oxygen")
    def feed(self):
        print("I eat food")

class Herbivorous(Animal):
    """def feed(self):
        #super().feed()
        print("I eat only plants")"""

herbi=Herbivorous()
herbi.feed()
