nums = [1,1,1,2,2,3]

def AllowAtmostTwoSuplicates(nums):
    slow = 2
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
        else:
           continue
    print(nums)
    return slow
print(AllowAtmostTwoSuplicates(nums))        