nums = [1,1,2,2,3,3,3,4]

def removeDuplicatesFromSortedArray(nums):
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] == nums[slow]:
            continue
        else:
            slow += 1
            nums[slow] = nums[fast]
    # print(nums)
    # slow represents the index for the last unique element
    # so number of unique elements = slow + 1
    return slow + 1

print(removeDuplicatesFromSortedArray(nums))