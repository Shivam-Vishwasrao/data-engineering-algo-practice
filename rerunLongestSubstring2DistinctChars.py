s = "eceba"
k = 2

def longestSubStringWithKDistinct(s, k):

    freq = {}
    left = 0
    max_length = 0
    distinct = 0
    length = 0

    # The first thing we need to do is, loop over the string, add it to dict if the char is distinct
    for right in range(len(s)):
        if s[right] not in freq:
            freq[s[right]] = freq.get(s[right], 0) + 1
            distinct += 1
            length += 1
        else:
            freq[s[right]] += 1
            length += 1
           
        # Now, handeling the condition break situation, when left window moves.
        while distinct > k:
            freq[s[left]] -= 1
            
            if freq[s[left]] == 0:
                del freq[s[left]]
                distinct -= 1
                left += 1
             
            max_length = max(right - left, max_length)
    print(len(freq))
    print(freq)
    return max_length

print(longestSubStringWithKDistinct(s, k))

# GPT Code

# def longestSubStringWithKDistinct(s, k):
#     freq = {}
#     left = 0
#     max_length = 0

#     for right in range(len(s)):
#         char = s[right]
#         freq[char] = freq.get(char, 0) + 1

#         while len(freq) > k:
#             left_char = s[left]
#             freq[left_char] -= 1

#             if freq[left_char] == 0:
#                 del freq[left_char]

#             left += 1

#         max_length = max(max_length, right - left + 1)

#     return max_length