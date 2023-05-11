def grow(arr):
    i = 0
    j = len(arr) - 1
    ans = 1

    while i <= j:
        if j == i:
            ans *= arr[i]
        else:
       	    ans *= arr[i] * arr[j]
        i += 1
        j -= 1

    return ans
