def isprime(x):
    for i in range(2, int((x ** 0.5)) + 1):
        if x % i == 0:
            return False
    return True

def isgprime(real,imag):
    return (
        (real == 0 and imag % 4 == 3)
        or (imag == 0 and real % 4 == 3)
        or isprime(real ** 2 + imag ** 2)
    )

if __name__ == "__main__":
    print(isprime(4))
