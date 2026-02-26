arr = [4,2,1,7,8,1,2,8,1,0]
k = 3

def runningSubStringAvg(arr, k):
    runningSum = sum(arr[0:k])
    runningAvg = ( runningSum / k)
    left = 0
    # maxAvg = 0 # we are making an assumption that the numbers are positive so setting equal
    # to zero works in this case, but if numbers in the arr were negative, then the max avg
    # would be negative in that case. So, its better ig you do maxAvg = runningSum/k. 
    # Great engineers think - "Does my initialization assume something about the input?"
    maxAvg = runningSum/k
    maxAvg = max(runningAvg, maxAvg)
    maxSum = runningSum

    for right in range(k, len(arr)):
        runningSum -= arr[left]
        left += 1
        runningSum += arr[right]
        # runningAvg = (runningSum / k)
        maxSum = max(runningSum, maxSum)

    # maxAvg = max(runningAvg, maxAvg)
    maxAvg = max((maxSum / k), maxAvg) # avoiding unnecessary floating ops inside loop
    
    return maxAvg

print(runningSubStringAvg(arr, k))



