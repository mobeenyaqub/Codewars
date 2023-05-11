def number_to_pwr(number, p):
    ans = 1
    for i in range(p):
        ans *= number

    return ans
