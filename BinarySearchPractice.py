nums = [2,4,6,8,10,12]

def binarySearch(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(binarySearch(nums, 8))