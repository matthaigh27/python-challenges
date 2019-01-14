import math
import time

def isprime(x):
    for i in range(2, round(math.sqrt(x))):
        if (x / i - math.floor(x / i)) == 0:
            return False
    return True

while True:
    x = for i in range()
    t = time.time()
    print(isprime(int(x)))
    print(time.time() - t)
