# nums = [4,5,6,7,0,1,2]
nums = [3,5,0,1,2]

def findMinimum(nums):

    left = 0
    right = len(nums) - 1

    while left < right:

        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return left

def findMaximum(nums):
    minIndex = findMinimum(nums)
    maxIndex = (minIndex - 1) % len(nums)

    return nums[maxIndex]

print(findMaximum(nums))