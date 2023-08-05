def triple_double(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    n1 = list(set(num1))
    check = False
    num = None
    
    for i in n1:
        if i * 3 in num1:
            num = i
            check = True
            break
        else:
            check = False

    if not check:
        return False

    return num * 2 in num2