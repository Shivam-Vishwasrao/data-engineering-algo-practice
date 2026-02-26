nums = [2, 7, 11, 15]
target = 9

my_dict = {}

def twoSum(num, target):
    for num in nums:
        complement = target - num

        if complement in my_dict:
            return(complement, num)
        
        my_dict[num] = True

# print(twoSum(nums, target))

char = 'z'
value = ord(char) - ord('a') + 1
print("Value", value)