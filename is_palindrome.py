def is_palindrome(s):
    text = list(s)
    l, r = 0, len(s) - 1
    
    while l < r:
        if text[l] != text[r]:
            return False
        l += 1
        r -= 1
    return True

print(is_palindrome("hello"))
print(is_palindrome("madam"))