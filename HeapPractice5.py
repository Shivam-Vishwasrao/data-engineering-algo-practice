import heapq

nums = [1,3,7,8,9]
target = 5
k = 2

def closestToTarget(list, t, k):

    heap = []
    distance = 0
    for num in list:
        
        distance = abs(num - target)
        # PUSH A TUPLE TO THE HEAP, -DISTANCE MAKES SURE THAT THE USE MAX HEAP AND THAT
        # THE NUMS FARTHEST FROM TARGET ARE REMOVED FIRST. THIS IS THE POWER OF HEAPS.
        # ITERATE + COMPUTE + COMPARE ALL AT THE SAME TIME. 
        # HEAP LOOKS AT TUPLES LEXICOGRAHICALLY, ELEMENT 1 IN TUPLE HAS PRIORITY, SO, 
        # HEAP WILL BE ORDERED BY ITEM 1 IN TUPLE, IF THERE IS A COLLISION THEN HEAP 
        # LOOKS AT ELEMENT 2.
        heapq.heappush(heap, (-distance, num))
        if len(heap) > k:
            heapq.heappop(heap)
        
    result = []
    for _, num in heap:
        result.append(num)

    return result

print(closestToTarget(nums, target, k))