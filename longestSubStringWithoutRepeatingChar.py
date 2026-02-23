S = "abcabcbb"

def longestSubString(s):
    maxSubstringLength = 0
    length = 0
    leftIndex = 0
    charSet = set()

    for i in range(len(s)):
        if s[i] not in charSet:
            charSet.add(s[i])
            length = i - leftIndex + 1
            maxSubstringLength = max(length, maxSubstringLength)
        else:
            while s[i] in charSet:
                charSet.remove(s[leftIndex])
                leftIndex += 1

            # Adding the new character after removing its duplicate 
            charSet.add(s[i])
            length = i - leftIndex + 1
            maxSubstringLength = max(length, maxSubstringLength)

    return("MaxSubStringLength: ", maxSubstringLength)

print(longestSubString(S))
