weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

def shipWithinDays(weights, days):
    left = max(weights)
    right = sum(weights)

    while left < right:

        mid = (left + right) // 2

        daysUsed = 1
        currentLoad = 0
        
        for weight in weights:
            if currentLoad + weight > mid:
                daysUsed += 1
                currentLoad = 0
            
            currentLoad += weight
        
        if daysUsed <= days:
            right = mid
        else:
            left = mid + 1
    
    return left

print(shipWithinDays(weights, days))