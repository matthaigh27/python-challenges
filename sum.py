def sum(*nums):
    print(nums)
    sum = 0
    for num in nums: # num becomes the numbers 1,2,3,4,5,6,7,8, etc.
        sum += num
    return sum

nums = [0, 1, 2, 3, 4, 5, 6]
print(sum(*nums))
