nums = [1,3,5,7,6,4,2]

def mountainArrayPeak(nums):
    left = 0
    right = len(nums) - 1

    while left < right:

        mid = (left + right) // 2

        # Find the peak of the mountain using Binary Search
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid # not mid - 1 because mid can be the peak too
    return left

print(mountainArrayPeak(nums))