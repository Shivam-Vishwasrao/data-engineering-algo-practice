arr = [2,1,5,2,3,2]
S = 7

def smallestContigiousSubArray(arr, S):
    left = 0
    minLength = float('inf')
    runningTotal = 0
    for right in range(len(arr)):
        runningTotal += arr[right]
        while runningTotal >= S: # keep moving right
            runningMinLength = right-left + 1
            runningTotal -= arr[left]
            left += 1
            minLength = min(runningMinLength, minLength)
    if (minLength == float('inf')):
        return 0
    return minLength

print(smallestContigiousSubArray(arr, S))
