import heapq
# PROB: FIND LARGEST ELEMENT USING HEAP. WE ARE NOT TO USE MAX() AND KEEP THE TIME 
#       COMPLEXCITY AS MIN AS POSSIBLE. SO WE TRICK THE HEAP, AS WE ENTER NUMBERS 
#       IN THE HEAP, WE CONVERT THEM TO NEGATIVE, SO THE LARGEST NUM IN ARR BCOMS THE
#       THE SMALLEST NUM IN HEAP, AND AT THE TIME OF POPPING, WE POP AND CONVERT BACK
#       TO POSITIVE. BY INSERTING -VE NUMS IN A HEAP WE TRICK A MIN HEAP TO ACT LIKE A
#       MAX HEAP! BEAUTIFUL, ISN'T IT?
 
nums = [5, 1, 9, 3, 7]

heap = []

for num in nums:
    heapq.heappush(heap, -num)

# Solution 1:
# log (n log n) complexcity! Long time processs!
# while len(heap) != 1:
#     heapq.heappop(heap)

# print(heap[0])

# Solution 2:
# Faster route O(n) time complexcity

print(heap) # Output - [-9, -7, -5, -1, -3]

print(heapq.heappop(heap) * -1) # Convert to positive




