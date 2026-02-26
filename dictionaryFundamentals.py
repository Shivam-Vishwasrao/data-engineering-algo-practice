nums = [1, 2, 2, 3, 3, 3, 4]
my_dict = {}

def dictionary(nums):
    for i in nums:
        my_dict[i] = my_dict.get(i, 0) + 1
    
    return my_dict

print(dictionary(nums))