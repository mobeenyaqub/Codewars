def added_char(s1, s2): 
    for i in sorted(set(s2)):
        if s2.count(i) > s1.count(i):
            return i