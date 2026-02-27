arr = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

# Valid condition: sum <= k 
# Invalid Condition: sum > k

def longestContigiousSubarrayWithSumLessThanEqualToK(arr, k):
    sum = 0
    maxLength = 0
    left = 0

    for right in range(len(arr)):
        sum += arr[right]

        # Now, handeling invalid condition
        while sum > k:
            sum -= arr[left]
            left += 1
        
        # Updating max length here because the conditon is valid outside the while loop
        maxLength = max(maxLength, right - left + 1)

    return maxLength

print(longestContigiousSubarrayWithSumLessThanEqualToK(arr, k))