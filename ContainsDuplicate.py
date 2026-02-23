nums = [1,2,3,1]
def containsDuplicates(nums):
    hashMap = {}

    for i, num in enumerate(nums):
        if num in hashMap:
            return True
        else:
            hashMap[num] = i
    
    return False

print(containsDuplicates(nums))