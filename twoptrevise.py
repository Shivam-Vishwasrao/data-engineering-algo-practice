numbers = [2,7,11,15]
target = 9

def twoSumSorter(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current = numbers[left] + numbers[right]

        if current == target:
            return left + 1, right + 1 # 1-based indexing
        
        if current < target:
            left += 1
        else:
            right -= 1
    
    return -1

print(twoSumSorter(numbers, target))