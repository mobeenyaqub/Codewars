def cut_the_ropes(arr):
    ans = [len(arr)]
    while arr:
        minn = min(arr)
        arr = [num - minn for num in arr if num - minn != 0]
        ans.append(len(arr))
    
    return ans[:-1]