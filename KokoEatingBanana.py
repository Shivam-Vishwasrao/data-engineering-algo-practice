import math
piles = [3,6,7,11]
h = 8

def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)

    while left < right:

        mid = (left + right) // 2
        hours = 0

        for pile in piles:
            hours += math.ceil(pile / mid)
        
        if hours <= h:
            right = mid
        else:
            left = mid + 1
    return left

print(minEatingSpeed(piles, h))