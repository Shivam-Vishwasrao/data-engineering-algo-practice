"""
left = 0
hashMap = {}

for right:
    add to hashMap[s[right]]

    # check invalid
    while len(hashMap) > k:
        hashMap[s[left]] -= 1

        if hashMap[s[left]] == 0:
            del hashMap[s[left]]
        left ++
    
    if len(hashMap) == k:
        update maxLenght

return MaxLength
"""
s = "aaabb"
k = 2

def LongstSubstrWithExactlykDistinctChars(s, k):
    left = 0
    hashMap = {}
    maxLength = 0

    for right in range(len(s)):
        hashMap[s[right]] = hashMap.get(s[right], 0) + 1

        # invalid condition (shrink here)
        while len(hashMap) > k:
            hashMap[s[left]] -= 1

            if hashMap[s[left]] == 0:
                del hashMap[s[left]]
            
            left += 1
        
        if len(hashMap) == k:
            maxLength = max(maxLength, right - left + 1)
        
    return maxLength

print(LongstSubstrWithExactlykDistinctChars(s, k))