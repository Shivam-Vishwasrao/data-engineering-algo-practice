n = [2, 1, 5]

def nextGreaterElement(n):
    stack = []
    result = [-1] * len(n)

    for i in range(len(n)):
        while stack and n[i] > n[stack[-1]]:
            index = stack.pop()
            result[index] = n[i] 
        
        stack.append(i)
    
    return result

print(nextGreaterElement(n))
