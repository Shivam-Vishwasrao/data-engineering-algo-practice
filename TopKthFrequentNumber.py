import heapq
nums = [2,2,3,3,3,4,4,5]
k = 2

####
# Step 1: Create dictionary to store number with their freq.
# Step 2: Create a min heap to store the num and freq pairs while limiting heap len to k
# Step 3: Create a list of nums with most freq in the heap
# ##

def kthMostFrequentNumber(nums, k):

    # Step 1
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
        # if num in frequency:
        #     frequency[num] += 1
        # else:
        #     frequency[num] = 1

    # Step 2: Create min heap with length k

    heap = []

    for num, freq in frequency.items():
        heapq.heappush(heap, (freq, num))

        if len(heap) > k:
            heapq.heappop(heap)

    # Step 3: resultant list to store nums with max occurances
    result = []

    for freq, num in heap: # you can also: for _, num in heap:
        result.append(num)

    return result

print(kthMostFrequentNumber(nums, k)) 