def gap(g, m, n):
    data = []
    for i in range(m, n + 1):
        check = True
        for j in range(2, round(i**0.5) + 1):
            if i % j == 0:
                check = False
                break

        if check:
            data.append(i)

        if len(data) > 1:
            if data[-1] - data[-2] == g:
                return [data[-2], data[-1]]

    return None
