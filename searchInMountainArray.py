nums = [1,3,5,7,6,4,2]
target = 4

def findPeak(nums):

    left = 0
    right = len(nums) - 1

    while left < right:

        mid = (left + right) // 2

        # Step 1 - Find peak

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

def searchTargetInMountain(nums, target):

    peakIndex = findPeak(nums)

    peakIndex = findPeak(nums)

    # Step 2 — Binary search left side (ascending)
    left = 0
    right = peakIndex

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1


    # Step 3 — Binary search right side (descending)
    left = peakIndex + 1
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            right = mid - 1   # reversed because descending

        else:
            left = mid + 1

        
    return -1

print(searchTargetInMountain(nums, target))
