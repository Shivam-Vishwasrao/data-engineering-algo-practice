nums = [0,1,0,3,12]

def moveZeros(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] == 0:
            continue
        else:
            nums[slow] = nums[fast]
            slow += 1
    # Fill remaining positions with Zero
    for i in range(slow, len(nums)):
        nums[i] = 0

    return nums
print(moveZeros(nums=nums))
    