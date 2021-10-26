
# after yield it will send value pause the func
# and in next call it will execute below stmt of prev yield
def gen():
    yield 1
    yield 2
    yield 3
    yield 4

values=gen()

print(next(values))
print(next(values))

for i in values:
    print(i)

def topten_Sq():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

print()
values=topten_Sq()

for val in values:
    print(val)