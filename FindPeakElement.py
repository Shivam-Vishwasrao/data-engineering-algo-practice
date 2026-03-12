# nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]
def findPeakElement(nums):

    left = 0
    right = len(nums) - 1

    while left < right: # < -> ensures mid + 1 is always valid and in bounds

        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            # move right, uphill -> peak on right
            left = mid + 1
        else:
            # move left, downhill -> peak on left
            right = mid # not mid - 1 -> b'coz mid itself might be the peak
    return left

print(findPeakElement(nums))