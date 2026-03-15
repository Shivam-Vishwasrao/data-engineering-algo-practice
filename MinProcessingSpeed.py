import math
tasks = [6,3]
hours = 3

def minProcessSpeed(tasks, hours):
    left = 1
    right = max(tasks)

    while left < right:
        mid = (left + right) // 2

        totalHours = 0

        for task in tasks:
            totalHours += math.ceil(task / mid)

        if totalHours <= hours:
            right = mid
        else:
            left = mid + 1

    return left
print(minProcessSpeed(tasks, hours)) 