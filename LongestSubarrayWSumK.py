arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
K = 8

def LongestSubArray(arr, k):
    minLength = float('inf')
    left = 0
    sum = 0

    for right in range(len(arr)):
        sum += arr[right]

        while sum >= k:
            minLength = right - left + 1 # We update when the window satisfies the problem condition!
            sum -= arr[left]
            left += 1
    
    if minLength == float('inf'):
        return 0
    
    return minLength

print(LongestSubArray(arr, K))