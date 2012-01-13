import math
import functools
import operator 

def sumFibo(n):
    return sum(i for i in fibo2(upto=n) if not i%2)

def fibo2(a=-1,b=1,limit=4000000):
    while a+b < limit:
        a,b = b,a+b
        yield b

if __name__ == "__main__":
    print "Sum of 4000000 fibonacci numbers: %d" % sumFibo(4000000)
