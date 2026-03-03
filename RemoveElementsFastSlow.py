nums = [3,2,2,3]
val = 3

def removeElements(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] == val:
            continue # skip it
        else:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow

print(removeElements(nums, val))        