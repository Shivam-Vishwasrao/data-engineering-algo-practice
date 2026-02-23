nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    my_hash = {} # Declaring hash map - python dictionary comes in key and value format

    for i, num in enumerate(nums):
        difference = target - num

        if difference in my_hash:
            return [my_hash[difference], i]
        
        my_hash[num] = i

print(twoSum(nums,target))
