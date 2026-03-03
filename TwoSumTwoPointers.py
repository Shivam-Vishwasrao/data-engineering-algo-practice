# nums = [2, 7, 11, 15]
# nums = [3,2,4]
nums = [4,1,6,8]
target = 9

def twoSums(arr, target):

    hashMap = {}

    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in hashMap:
            return hashMap[complement], i
        else:
            hashMap[arr[i]] = i
    
    return -1

print(twoSums(nums, target))
        