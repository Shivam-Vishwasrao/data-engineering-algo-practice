pages = 120
hours = 10

def minimumStudySpeed(pages, hours):
    left = 1
    right = pages

    while left < right:
        mid = (left + right) // 2

        if mid * hours >= pages:
            right = mid
        else:
            left = mid + 1
    
    return left
print(minimumStudySpeed(120, 10))