nums = [2,1,5,1,3,2]
k = 3

def maxSumSubarray(nums, k):

    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum = current_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, current_sum)
    print(max_sum)
    return max_sum 

maxSumSubarray(nums, k)