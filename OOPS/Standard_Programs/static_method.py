class FixedFloat:
    def __init__(self,amount):
        self.amount=amount
    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>

    @staticmethod
    def from_sum1(v1,v2):
        return FixedFloat(v1+v2)


class Euro(FixedFloat):
    def __init___(self,amount):
        super().__init__(amount)
        self.symbol='e'

    def __repr__(self):
        return f"<Euro {self.symbol} {self.amount:.2f}"

num1=FixedFloat.from_sum1(19.8,10.67)
print(num1)
num2=Euro.from_sum1(18.90,17.89)
print(num2)
