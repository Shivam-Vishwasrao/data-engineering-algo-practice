"""
Input:  "abcabcbb"
Output: 3

Pseudo Code:

left = 0
charSet = empty set
maxLength = 0

# Expand the window
for every char on right

    while s[right] is in charSet:
        remove s[left] from charSet
        left +=1
    
    add s[right] to charSet

    update maxLenght = max (maxLength, right-left+1)
return maxLength
"""
# s = "abcabcbb"
s = "abba"

def LongestSubStrinWithoutRepetation(s):

    maxLength = 0
    left = 0
    subStringSet = set()

    for right in range(len(s)):

        while s[right] in subStringSet:
            subStringSet.remove(s[left])
            left += 1
        
        subStringSet.add(s[right])

        maxLength = max(maxLength, right - left + 1)

    return maxLength

print(LongestSubStrinWithoutRepetation(s))
