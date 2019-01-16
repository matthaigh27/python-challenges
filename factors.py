def fact(x):
    factors = [1]
    start = 2
    c = 0
    while x != 1:
        for div in range(start,x // 2 + 1):
            print(x,div)
            c += 1
            if x % div == 0:
                factors.append(div)
                start = div
                x = x // div
                break
            elif div == x // 2:
                factors.append(x)
                print(c)
                return factors
    print(c)
    return factors
print(fact(7))