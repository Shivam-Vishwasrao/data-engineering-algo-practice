"""
Input:  s = "eceba", k = 2
Output: 3
Explanation: "ece"

Valid: When distinct chars in substring are k
Invalid: When distinct chars in substring are greater of less than K

Pseudo Code:

left = 0
maxLength = 0
charFreq = {}
distinct = 0

for right:
    add char to charFreq
    distinct ++

    while distinct > k
        charFreq[left] -= 1
        if count becomes 0:
            remove it from hashmap
        left ++

    maxLength - max(maxLength, right - left + 1)

return maxLength 
"""
s = "ebeca"
k = 2
def LongestSubstringwithAtMostKDistinctChars(s, k):

    maxLenght = 0
    left = 0
    hashMap = {}

    for right in range(len(s)):
        #       KEY       =         VALUE
        hashMap[s[right]] = hashMap.get(s[right], 0) + 1

        # Invalid condition
        while len(hashMap) > k:
            hashMap[s[left]] -= 1

            if hashMap[s[left]] == 0:
                del hashMap[s[left]]
            
            left += 1 # incrementing left evertime we shrink
        
        maxLenght = max(maxLenght, right - left + 1)
    
    return maxLenght

print(LongestSubstringwithAtMostKDistinctChars(s, k))