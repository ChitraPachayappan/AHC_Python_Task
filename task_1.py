def sumof_3n5(n):
    total = 0
    for i in range(n):
        if i%3 == 0 or i%5==0:
            total += i
    return total


sumof_3n5(1000)