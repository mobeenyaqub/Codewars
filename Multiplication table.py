def multiplication_table(size):
    ans = []
    s = []
    j = 1
    x = 0
    for i in range(1, size**2 + 1):
        s.append(j+x)
        if len(s) == size:
            ans.append(s.copy())
            s.clear()
            j += 1
            x = 0
        else:
            x += j

    return ans
