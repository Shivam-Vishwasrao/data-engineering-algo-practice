arr = [2, 1, 5, 2, 8]
k = 7

# arr = [2, 1, 5, 2, 3, 2]
# k = 7

# return smallest length of cotiguous subArray
# valid - sum >= k (expand + update length)
# Invalid - sum < k (shrink till valid)
# for right in arr
#   add right to sum
#
#   while sum >= k:
#       sum -= arr[left]
#       left += 1
#       updaet shortest length for which the condition is still valid

def smallestLengthWithSumK(arr, k):
    sum = 0
    left = 0
    shortestLength = float('inf') # Verify: Is this assumption correct, Shivam?
    bestStart = 0
    bestEnd = 0
    runningLength = 0

    for right in range(len(arr)):
        sum += arr[right]

        while sum >= k:
            runningLength = right - left + 1

            # only update when strictly smaller
            if runningLength < shortestLength:
                shortestLength = runningLength
                bestStart = left
                bestEnd = right
            
            # Now shrink
            sum -= arr[left]
            left += 1
    
    if shortestLength == float('inf'):
        return 0.0, []
    
    return shortestLength, arr[bestStart:bestEnd + 1]

print(smallestLengthWithSumK(arr, k))