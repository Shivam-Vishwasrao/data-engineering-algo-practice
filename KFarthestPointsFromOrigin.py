import heapq
points = [[1,3], [-2,2], [5,8], [0,1]]
k = 2

def KFarthestPointsFromOrigin(points, k):

    heap = []
    for x,y in points:
        dist = x*x + y*y

        # Push the dist to min heap
        heapq.heappush(heap, (dist, x,y))

        # Maintain the heap size continiously
        if len(heap)> k:
            heapq.heappop(heap)

    result = []
    for __,x,y in heap:
        result.append([x,y])
    
    return result

print(KFarthestPointsFromOrigin(points, k))