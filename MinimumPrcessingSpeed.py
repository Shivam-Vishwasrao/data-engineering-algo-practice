import math
items = [2,3]
hours = 2

def minimumProcessingSpeed(items, hours):
    left = 1
    right = max(items)

    while left < right:

        mid = (left + right) // 2 # mid represents the speed
        hoursSpent = 0
        for task in items:

            hoursSpent += math.ceil(task / mid)

        if hoursSpent <= hours:
            right = mid
        else:
            left = mid + 1
    return left

print(minimumProcessingSpeed(items, hours))
