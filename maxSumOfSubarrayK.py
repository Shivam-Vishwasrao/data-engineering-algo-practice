arr = [2,1,5,1,3,2]
k = 3

def maxSum(arr, k):
    maxSum = 0
    currentWindow = arr[0:k]
    runningSum = sum(currentWindow)
    maxSum = max(runningSum, maxSum)
    left = 0
    for right in range(k, len(arr)):
        runningSum -= arr[left]
        runningSum += arr[right]
        left += 1
        maxSum = max(runningSum, maxSum)

    return maxSum

print(maxSum(arr, k))
