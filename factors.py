def fact(x):
    if x != 1:
        for div in range(2, x // 2 + 1):
            if x % div == 0:
                factors.append(div)
                factors.append(x//div)
                return fact(x // div)
            elif div == x // 2 and x % div != 0:
                return fact(1)
    else:
        fac = str(factors)
        factors.clear()
        return fac


factors = []
print(fact(3))
