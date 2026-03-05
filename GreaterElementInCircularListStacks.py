nums = [1,2,1]

def nextGreaterElementCircularList(nums):
    stack = []
    results = [-1] * len(nums)

    for i in range(2 * len(nums)):
        current = nums[i % len(nums)] # simulates the wrapping around effect in circular list
        while stack and current > nums[stack[-1]]:
            index = stack.pop()
            results[index] = current
        
        # only push indices during first pass
        if i < len(nums):
            stack.append(i)
    
    return results

print(nextGreaterElementCircularList(nums))
