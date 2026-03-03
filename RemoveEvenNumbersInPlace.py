# nums = [1,2,3,4,5] 
nums = [2,4,6,8]

def removeEvenNumbers(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] % 2 == 0:
            continue
        else:
            nums[slow] = nums[fast]
            slow += 1
    print(nums)
    return slow

print(removeEvenNumbers(nums))