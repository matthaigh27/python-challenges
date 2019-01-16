L = 999
R = 999
p = 1
c = 0
geo = 111
cond = True

while(cond):
    c += 1
    # print(R)
    if L > 111:
        L -= 1
        if str(L * R) == str(L * R)[::-1]:
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