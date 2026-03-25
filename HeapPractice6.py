import heapq

nums = [1,3,7,8,9]
target = 5
k = 2

def KFarthestElement(list, t, k):
    heap = []

    for num in list:
        distance = abs(target - num)

        heapq.heappush(heap, (distance, num))

        if len(heap) > k:
            heapq.heappop(heap)
    result = []
    for _, num in heap:
        result.append(num)
    
    return result
print(KFarthestElement(nums, target, k))