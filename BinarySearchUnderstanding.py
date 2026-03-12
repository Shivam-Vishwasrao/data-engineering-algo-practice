# NOTE: BINARY SEARCH ONLY WORKS IF THE DATA IS SORTED
list = [1,3,5,7,9,11]

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
print(binarySearch(list, 7))