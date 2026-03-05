from collections import deque
tasks = ["Task1", "Task2", "Task3"]

def taskProcessor(tasksList):
    queue = deque()

    # Enqueue tasks
    for task in tasksList:
        queue.append(task)

    # dequeue tasks
    while queue:
        t = queue.popleft()
        print("Processing", t)    
    
    if not queue:
        print("All tasks completed")

taskProcessor(tasks)