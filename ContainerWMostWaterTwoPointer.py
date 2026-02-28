height = [1,8,6,2,5,4,8,3,7]

def mostWaterInCountainer(arr):
    left = 0
    right = len(arr) - 1
    width = 0
    height = 0
    area = 0
    
    while left < right:
        width = right - left # distance between 2 indices on x-axis
        height = min(arr[right], arr[left]) # min because the capacity is dictated by the shorter wall
        area = max(area, width * height)

        # Move the shorter wall
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    
    return area

print(mostWaterInCountainer(height))
