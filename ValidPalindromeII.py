# s = "abca"
# s = "deeee"
# s = "hello"
s = "abc"

def helper(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindromeII(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return helper(s, left + 1, right) or helper(s, left, right-1)
    
        left += 1
        right -= 1
    return True

print(isPalindromeII(s))