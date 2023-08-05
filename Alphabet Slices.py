def solution(s):
    ans = []
    initial = s[0]
    word = initial
    for i in s[1:]:
        if ord(initial) + 1 == ord(i):
            word += i
            initial = i
        else:
            ans.append(word[::-1])
            word = initial = i

    ans.append(word[::-1])

    return ''.join(ans)