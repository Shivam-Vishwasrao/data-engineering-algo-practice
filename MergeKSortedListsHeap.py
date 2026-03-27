import heapq
lists = [
    [1,4,5],
    [1,3,4],
    [2,6]
]


def MergeKSortedLists(lists):
    heap = []
    result = []

    # Step 1: Initialize heap with first element of each list
    for listIndex in range(len(lists)):
        if len(lists[listIndex]) > 0:
            value = lists[listIndex][0]
            heapq.heappush(heap, (value, listIndex, 0))
    # Step 2: Process heap
    while heap:
        value, listIndex, elementIndex = heapq.heappop(heap)
        result.append(value)

        nextIndex = elementIndex + 1

        # If next element exists in the same list
        if nextIndex < len(lists[listIndex]):
            nextValue = lists[listIndex][nextIndex]
            heapq.heappush(heap, (nextValue, listIndex, nextIndex))

    return result

print(MergeKSortedLists(lists))