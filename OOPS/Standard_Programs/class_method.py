class FixedFloat:
    def __init__(self,amount):
        self.amount=amount
    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @classmethod
    def from_sum1(cls,v1,v2):
        return cls(v1+v2)


class Euro(FixedFloat):
    def __init__(self,amount):
        self.s="E"
        super().__init__(amount)
    def __repr__(self):
        return f"<Euro {self.s} {self.amount:.2f}"

num1=FixedFloat.from_sum1(19.8,10.67)
print(num1)
num2=Euro.from_sum1(18.90,17.89)
print(num2)
