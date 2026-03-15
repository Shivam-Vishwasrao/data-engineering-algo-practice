pages = 500
hours = 20

def minPrintingSpeed(pages, hours):
    left = 1 # printer prints 1 page/hour, worst case scenario
    right = 500 # 500 pages/hour, best case scenario

    while left < right:

        mid = (left + right) // 2

        if mid * hours >= pages: # too fast
            right = mid
        else: # too slow
            left = mid + 1
    return left

print(minPrintingSpeed(pages, hours))
        