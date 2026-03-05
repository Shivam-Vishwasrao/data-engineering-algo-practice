from collections import deque

line = ["Alice", "Bob", "Charlie"]

def ticketCounter(line):
    queue = deque()
    
    # enqueue
    for customer in line:
        queue.append(customer)
    
    # dequeue properly (FIFO)
    while queue:
        customer = queue.popleft()
        print("Serving", customer)

print(ticketCounter(line))

