s = "(){}[]"

def isValid(s):

    myStack = [] # Creating empty stack
    pairs = {
        ')' : "(",
        '}' : '{',
        ']' : '[',
    }

    for char in s:
        if char in pairs:
            # If closing bracket
            if not myStack:
                # If list is empty return False immediately since this is closing bracket
                return False
            if myStack[-1] == pairs[char]:
                myStack.pop()
            else:
                return False
        else:
            # opening bracket
            myStack.append(char)
    
    print(myStack)
    return len(myStack) == 0

print(isValid(s))
