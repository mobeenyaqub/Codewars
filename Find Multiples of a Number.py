def find_multiples(integer, limit):
    i = integer
    ans = [i]

    while True:
        i += integer
        if i > limit:
            break
        ans.append(i)

    return ans
