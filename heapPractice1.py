import heapq

heap = []

heapq.heappush(heap, 5)
print(heap)
heapq.heappush(heap, 2)
print(heap)
heapq.heappush(heap, 8)
print(heap)
heapq.heappush(heap, 1)
print(heap)

# Smallest element print
print(heap[0])

# Remove element one by one and print them
while heap:
    print(heapq.heappop(heap))

