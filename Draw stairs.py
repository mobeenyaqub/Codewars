def draw_stairs(n):
    ans = ""
    for c in range(n):
        i = "I\n" if c != n-1 else "I"
        ans += c * " " + i
    
    return ans