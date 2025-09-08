def reverse_string(s):
    n = len(s)
    l = 0
    r = n - 1
 
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    
    return s

print(reverse_string(["h", "e", "l", "l", "o"]))