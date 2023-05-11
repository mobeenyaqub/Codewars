def quadrant(x, y):
    if 0 < x and 0 < y:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3

    return 4
