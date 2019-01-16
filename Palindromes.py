L = 999
R = 999
cond = True
p = 1
c = 0
geo = 111


def rev(x):
    return x[::-1]


while(cond):
    c += 1
    # print(R)
    if L > 111:
        L -= 1
        if str(L * R) == rev(str(L * R)):
            if L * R > p:
                geo = (L * R) ** 0.5 // 1
                p = L * R
                Rp = R
                Lp = L
    else:
        if R == geo:
            print("Palindrome:", p)
            print("Product:", Lp, "x", Rp)
            cond = False
        else:
            R -= 1
            L = R
print("Number of loops:",c)