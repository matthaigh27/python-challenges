import time
import primes

def sleep(t):
    time.sleep(t)

def timeit(func,a):
    start = time.time()
    ret = func(a)
    return (time.time() - start, ret)

print(timeit(primes.isprime, 32416190071))
