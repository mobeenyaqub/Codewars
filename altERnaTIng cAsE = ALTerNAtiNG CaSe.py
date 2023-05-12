def to_alternating_case(string):
    ans = ""
    for i in range(len(string)):
        if string[i].isupper():
            ans += string[i].lower()
        else:
            ans += string[i].upper()

    return ans
