data=[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600]
#print(len(li))
l=len(data)
size=l//2
print(size)

# swap len//2 times (it gives floor)
# reverse the list without using extra list
for i in range(0,size,1):
    temp=data[l-1]
    data[l-1]=data[i]
    data[i]=temp
    l=l-1

print("After reversed:",data)


start=0
end=5
res=data[start:end:1]
print(res)

chunksize=int(len(data)//3)
start=0
end=chunksize
for i in range(1,4,1):
    chunklist=data[start:end:1]
    start=end
    end=end+chunksize
    print("original:",chunklist,"Reversed chunklist:",list(reversed(chunklist)))

# num of times 'raghu' appear in string

def count_raghu(st):
    count=0
    for i in range(len(st)):
        if st[i:i+5]=='raghu':
            count+=1
    return count

st="hello raghu welcome raghu to indai hi raghu"
print(count_raghu(st))

# check palindrom 121,5225 both way reads same
def is_palindrom(num):
    rem=0
    reverse=0
    original=num
    while num>0:
        rem=num%10
        reverse=reverse*10+rem
        num=num//10
    if reverse==original:
        return True
    else:
        return False
print(is_palindrom(5225))
print(is_palindrom(132))
print()

# armstrong number 153-> 1^3+5^3+3^3=1+125+27=153

def digits(num):
    i=0
    while num>0:
        num=num//10
        i+=1
    print(f"digits are:{i}")
    return i

# rem 5 digits=3 i=0->1*5
#i=1->5*5, i=2 ->25*5
def powerof(rem,digits):
    base=1
    for i in range(digits):
        base=base*rem
    print(f"{rem} resto {digits}:{base}")
    return base

def is_armstrong(num):
    original=num
    print(f"Original num is:{num}")
    d=digits(num)
    rem=0
    sum=0
    while num>0:
        rem=num%10
        powered=powerof(rem,d)
        sum=sum+powered
        num=num//10
    if original==sum:
        print(f"sum is:{sum}")
        return True
    else:
        print(f"sum is:{sum}")
        return False

print(is_armstrong(153))
print(is_armstrong(123))

# count occurance of item
string="Hello WQorld"
count={}
for ch in string:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1

print(count)

# check is powerOf3

def is_powerOf3(num):
    temp=num
    while num!=1:
        if num%3!=0:
            return False
        num=num//3
    return True

print(is_powerOf3(24))
print(is_powerOf3(27))

# check perfect square
def is_perfect_square(num):
    x=num//2
    y=set([x])
    while x*x!=num:
        x=(x+(num//x))//2
        if x in y:
            return False
        else:
            y.add(x)
    return True

print(is_perfect_square(16))
print(is_perfect_square(10))

# fibonacci sequnec nterms
def fibonacci(nterms):
    n1,n2,count=0,1,0
    if nterms==1:
        print('fibo seq:',1)
    else:
        print('fiblo seq:')
    while count<=nterms:
        print(n1,end=" ")
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1

fibonacci(10)

print("recursive:")
def fib(nth):
    if nth==0:
        return 0
    if nth==1:
        return 1
    return fib(nth-1)+fib(nth-2)

print(fib(10))

def fibo_dynamic(nth):
    f=[]
    f.append(0)
    f.append(1)
    for i in range(2,nth+1,1):
        res=f[i-1]+f[i-2]
        f.append(res)
    print(f)
    return f[nth]

print(fibo_dynamic(10))

# factorial

def factorial(num):
    fact=1
    if num<=1:
        print("fact is:",1)
    else:
        for i in range(1,num+1):
            fact=fact*i
    print(f"fact of {num} is :{fact}")

factorial(5)    
# check given seq is fibo or not
seq1="6,6,12,18,30,48"
seq2="6,1,5,12,3,4"
seq3="0,1,1,2,5,7,8"


def is_fibo(seq):
    data=seq.split(",")
    n1,n2,n3,nth=0,0,0,0
    for i in range(len(data)-2):
        if n3==nth:
            print()
            print(f"upper:n3:{n3},nth:{nth},n1:{n1},n2:{n2}")
            n1=int(data[i])
            n2=int(data[i+1])
            n3=int(data[i+2])
            nth=n1+n2
            #print(f"lower:n3:{n3},nth:{nth},n1:{n1},n2:{n2}")
        else:
            return False
    return True

print()
print(is_fibo(seq1))
print(is_fibo(seq2))
#print(is_fibo(seq3))

n1=10
n2=9
print(n1^n2)


li=[1,2,4,6,8,10]
original=[x for x in range(li[0],li[-1]+1)]
print(f"given list:{li},continues:{original}")
li_set=set(li)
original_set=set(original)
print(original_set.difference(li_set))


print(original_set^li_set)

def dec_bin(num):
    rem=0
    li=[]
    while num>0:
        rem=num%2
        li.append(rem)
        num=num//2
    print(li)
    for i in range(len(li)-1,-1,-1):
        print(li[i],end="")

dec_bin(10)
    

