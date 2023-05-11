def solution(s):
    if len(s) % 2 == 0:
        return [s[i]+s[i+1] for i in range(0, len(s), 2)]
    else:
        ans = [s[i]+s[i+1] for i in range(0, len(s)-1, 2)]
        ans.append(s[-1] + "_")
        return ans
