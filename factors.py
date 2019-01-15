def fact(x):
    factors = []
    cond = True
    while(cond):
        if x // 2 + 1 == 2:
            factors.append(2)
            return factors
        else:
            for div in range(2,x // 2 + 1):
                if x % div == 0:
                    factors.append(div)
                    x = x // div
                    break
                elif div == x // 2:
                    factors.append(x)
                    return factors
print(fact(64))