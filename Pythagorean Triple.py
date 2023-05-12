# input is an unsorted list of 3 positive integers
def pythagorean_triple(i):
    if i[0]**2 + i[1]**2 == i[2]**2:
        return True
    if i[0]**2 + i[2]**2 == i[1]**2:
        return True
    if i[1]**2 + i[2]**2 == i[0]**2:
        return True

    return False
