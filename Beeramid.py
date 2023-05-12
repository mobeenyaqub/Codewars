def beeramid(bonus, price):
    cans = bonus // price
    i = 1
    count = 0
    while i**2 <= cans:
        cans -= i**2
        i += 1
        count += 1

    return count