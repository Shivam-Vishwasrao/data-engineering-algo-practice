nums = [4,5,6,7,0,1,2]

def findMinimum(nums):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]: # minimum is to the right
            left = mid + 1
        right = mid # minimum is to the left including mid

        return nums[left]
    
print(findMinimum(nums))