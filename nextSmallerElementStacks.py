nums = [4,8,5,2,25]

def nextSmallestElement(nums):
    stack = [] # storing indices of nums till next smallest not found
    result = [-1] * len(nums)

    for i in range(len(nums)):
        if not stack:
            stack.append(i)
        else:
            while stack and nums[i] < nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i]
            
            stack.append(i)
    return result

print(nextSmallestElement(nums)) 