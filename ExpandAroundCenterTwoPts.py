"""
Input: "babad"
Output: "bab" or "aba"
"""

"""
Input: string s
if length < 2:
    return s

longestStart = 0
longestLength = 1

for each i from 0 to len(s)-1:
    # Check odd palindrome
    Expand from (i,i)
    Get length1

    # Check even palindrome
    Expand(i, i+1)
    Get length2

    currMax = max(length1, length2)

    if currMax > longestLength:
        update longestLength
        update LongestStart

return substring from longetStart of size longestLength

define expand(left, right):
    while:
        left >=0
        right < len(s)
        s[left] == s[right]

        move left leftwards
        move right rightwards
    return length of palindrome found

"""
s = "racecar"

def ExpandAroundCenter(s):
    longestStart = 0
    longestLength = 1

    if len(s) < 2:
        return s
    
    # define expand function
    def expand(left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):

        # Call expand for odd case
        length1 = expand(i, i)

        # Call expand for even case
        length2 = expand(i, i+1)

        currMax = max(length1, length2)

        if currMax > longestLength:
            longestLength = currMax
            longestStart = i - (currMax - 1) // 2

    return s[longestStart: longestStart + longestLength] 

print(ExpandAroundCenter(s))

"""

def expand(left, right):
    while left >= 0 and right < len(S) and s[left] == s[right]
        left -= 1
        right += 1
    return left+1, right-1
"""
a = "racecar"
print(a[0:6+1])