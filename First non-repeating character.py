def first_non_repeating_letter(s):
    ss = s.lower()
    ans = ""

    for i in range(len(ss)):
        if ss.count(ss[i]) == 1:
            return s[i]

    return ans
