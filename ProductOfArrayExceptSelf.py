nums = [1,2,3,4]

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    # Left pass
    leftProduct = 1
    for i in range(n):
        result[i] = leftProduct
        leftProduct *= nums[i]

    # Right pass
    rightProduct = 1
    for i in range(n - 1, -1, -1):
        result[i] *= rightProduct
        rightProduct *= nums[i]

    return result

print(productExceptSelf(nums))