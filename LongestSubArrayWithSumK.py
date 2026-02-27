# arr = [2, 1, 5, 2, 3, 2]
# k = 7

arr = [1, 2, 1, 1, 1, 3, 2, 1]
k = 4

"""
Expected:
Longest Sub array (max variable)
sum of elements in subarray == k : valid
(sum > k) or (sum < k) : invalid

left = 0
sum = 0
maxLength = 0

for right in range(n):
    sum += arr[right]

    while sum > k:
        sum -= arr[left]
        left += 1

    if sum == k:
        update maxLength
"""
def longestSubArrayWithLengthEqualToK(arr, k):
    left = 0
    sum = 0
    maxLength = 0
    currentLength = 0
    bestStart = 0
    bestEnd = 0

    for right in range(len(arr)):
        sum += arr[right]

        while sum > k:
            sum -= arr[left]
            left += 1
        
        if sum == k:
            currentLength = right - left + 1
            if currentLength > maxLength:
                maxLength = currentLength
                bestStart = left
                bestEnd = right
            # maxLength = max(maxLength, currentLength)
    
    return maxLength, arr[bestStart:bestEnd + 1]

print(longestSubArrayWithLengthEqualToK(arr, k))