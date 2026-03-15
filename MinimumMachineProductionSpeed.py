items = 200
hours = 20

def minimumMachineSpeed(items, hours):
    left = 1
    right = items

    while left < right:
        mid = (left + right) // 2

        if mid * hours >= items:
            # Works! Lets reduced the speed to see if it works for smaller speed
            right = mid
        else:
            left = mid + 1
    return left
print(minimumMachineSpeed(200, 20))