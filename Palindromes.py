left = 99999999
right = 99999999
palindrome = 1
counter = 0
geo = 11111111
cond = True

while(cond):
    counter += 1
    if left > geo:
        left -= 1
        if str(left * right) == str(left * right)[::-1]:
            if left * right > palindrome:
                geo = (left * right) ** 0.5 // 1
                palindrome = left * right
                best_right = right
                best_left = left
                right -= 1
                left = right
    else:
        if right == geo:
            print("Palindrome:", palindrome)
            print("Product:", best_left, "x", best_right)
            cond = False
        else:
            right -= 1
            left = right
print("Number of loops:", counter)