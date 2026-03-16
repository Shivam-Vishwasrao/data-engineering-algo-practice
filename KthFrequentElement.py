import heapq
nums = [1,1,1,2,2,3]
k = 2

def kthMostFrequent(nums, k):

    frequency = {} # Dictionary

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    heap = []

    for num, freq in frequency.items():
        heapq.heappush(heap, (freq, num))

        if len(heap) > k:
            heapq.heappop(heap)
    
    result = []

    for freq, num in heap:
        result.append(num)
    
    return result

print(kthMostFrequent(nums, k))
