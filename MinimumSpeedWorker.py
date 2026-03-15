distance = 100
hours = 10

def minSpeed(distance, hours):

    left = 1
    right = distance

    while left < right:

        mid = (left + right) // 2

        if mid * hours >= distance:
            right = mid
        else:
            left = mid + 1

    return left
print(minSpeed(distance, hours))
            