import heapq
points = [[1,3], [-2,2], [5,8]]
k = 2

def KClosestPointToOrigin2D(points, k):

    heap = []
    # THINK OF POINTS AS (X,Y) ON GRAPH. WHICH MAKES THE ORIGIN TO BEING (0,0). WE WANT THE
    # POINTS THAT ARE CLOSES TO (0,0). IN 2D, DISTANCE IS CALCULATED USING PYTHAGORAS THEORM
    # ROOT OD X*X + Y*Y. BEACAUSE WE ARE COMPARING AND NOT COMPUTING ANYTHING FURTHER WITH THE
    # DISTANCE WE FIND. WE WILL SKIP THE SQRT PART BECAUSE THE ANS WILL BE THE SAME. 

    # WE WANT THE CLOSEST POINTS, SO, INSIDE OUR HEAP, WE NEED TO DELETE THE FARTHEST DIST.
    # I.E. USE MAX HEAP.
    
    for x,y in points:
        dist = x*x + y*y

        # Max heap simulation
        heapq.heappush(heap, (-dist, x, y))

        if len(heap) > k:
            heapq.heappop(heap)

    result = []

    for _,x,y in heap:
        result.append([x,y])
    
    return result

print(KClosestPointToOrigin2D(points, k))
