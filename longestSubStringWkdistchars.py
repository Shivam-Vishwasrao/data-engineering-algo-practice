s = "eceba"
k = 2

def longestSubStringWKDistinctChars(s, k):
    left = 0
    maxLength = 0
    charCount = {}

    for right in range(len(s)):

        # add current character
        charCount[s[right]] = charCount.get(s[right], 0) + 1

        # if we exceed k distinct characters, shrink window
        while len(charCount) > k:
            charCount[s[left]] -= 1

            if charCount[s[left]] == 0:
                del charCount[s[left]]
            
            left += 1

        # update max length
        maxLength = max(maxLength, right - left + 1)

    return maxLength

print(longestSubStringWKDistinctChars(s, k))
