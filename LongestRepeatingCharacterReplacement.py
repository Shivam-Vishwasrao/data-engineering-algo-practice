s = "AABABBA"
k = 1

def characterReplacement(s, k):
    count = {}
    left = 0
    max_freq = 0
    max_length = 0

    # expand window to the right, left and right are at index 0 right now.
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

        # If window invalid (window-size - max_freq > k) , shrink from left
        while(right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        # update answer
        max_length = max(max_length, right - left + 1)

    return max_length

characterReplacement(s, k)