def typist(s):
    char = s[0]
    count = 0 if char.islower() else 1
    for i in s[1:]:
        if (char.islower() and i.isupper()) or (char.isupper() and i.islower()):
            count += 1
            char = i
    
    return len(s) + count