def add(*nums):
    sum = 0
    for num in nums:
        sum += num 
    return sum

print(add(1, 4, 5, 7))