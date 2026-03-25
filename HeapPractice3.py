import heapq

nums = [5,1,9,3,7]
k = 2

def maxElementsInHeap(arr, n):

    heap = []

    # THE OBSERVATION OVER HERE IS THAT HEAP ARRANGES ITSELF IN A WAY WHERE THE SMALLEST
    # NUMBER ALWAYS FINDS ITS WAY TO ELEMENT 0 IN HEAP, SO, WEHEN WE POP, WE CAN BE SURE
    # THAT THE SMALLEST NUM IS BEING POPPED AND SINCE WE CARE FOR K LARGEST NUMS, WE ARE
    # UNDER PROTECTION AS LONG AS WE KEEP THAT IF LOOP THAT REGULATES HEAP SIZE.
    for num in arr:
        heapq.heappush(heap, num)

        if len(heap) > n:
            heapq.heappop(heap)
    
    return heap

print(maxElementsInHeap(nums, k))