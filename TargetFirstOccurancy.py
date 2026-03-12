nums = [1,2,2,2,3,4]
target = 2

def firstOccurance(nums, target):

    left = 0
    right = len(nums) - 1
    recordIndex = -1
    
    while left <= right:

        mid = (left+right)//2 
        if nums[mid] == target:
            recordIndex = mid
            right = mid - 1 # keep searching left

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return recordIndex

print(firstOccurance(nums, target))