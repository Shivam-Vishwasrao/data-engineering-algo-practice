nums = [1,2,2,2,3,4]
target = 2

def lastOccurance(nums, target):

    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:

        mid = (left+right)//2

        if nums[mid] == target:
            left = mid + 1
            result = mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return result

print(lastOccurance(nums, target))