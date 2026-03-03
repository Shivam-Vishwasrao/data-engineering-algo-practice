nums = [1, 7, 3, 9, 4, 6]

def replaceNumbersGrtrThanFiveInPlace(nums):

    slow = 0
    for fast in range(len(nums)):
        if nums[fast] > 5: # Fast looks for valid, if found, slow = fast.
            continue
        else:
            nums[slow] = nums[fast]
            slow += 1
    print(nums)
    return slow

print(replaceNumbersGrtrThanFiveInPlace(nums))