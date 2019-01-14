import primes
cond = True
x = 20 #find all purely complex primes with a,b up to x
a = x
b = x

while(cond):
    if a != 0:
        if primes.isprime(a**2 + b**2) == True:
            print(a, "+",str(b) + "i")
        a -= 1
    elif a == 0:
        if b != 1:
            b -= 1
            a = 50
        else:
            cond = False
