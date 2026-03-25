import heapq
nums = [5,1,9,3,7]
k = 2

def heapKSmallestElements(list, n):
    heap = []
    ###
    # HEAPS BY DEFAULT ARE MIN HEAPS, BUT, BEACUSE WE WANT THE K MIN ELEMENTS IN HEAP,
    # WE WILL REVERSE THE HEAP BY CONVERTING IT INTO A MAX HEAP BY INSERTING -VE NUMS
    # IN THE HEAP, AND THEN AT THE END, WE WILL MULTIPLY EACH ELEMENT IN HEAP BY -1
    # TO CONVERT THE HEAP BACK TO POSITIVE NUMBERS WHERE WE HAVE K SMALLEST NUMBERS 
    # LEFT IN THE HEAP.


    for num in list:
        heapq.heappush(heap, -num)

        if len(heap) > n:
            heapq.heappop(heap)

    return [-x for x in heap]

print(heapKSmallestElements(nums, k))
    