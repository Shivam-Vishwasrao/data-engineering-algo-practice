nums = [1,1,2]

def removeDuplicatesFromSortedArray(nums):

    if len(nums) == 0:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]: # We found a unique element
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

print(removeDuplicatesFromSortedArray(nums))
