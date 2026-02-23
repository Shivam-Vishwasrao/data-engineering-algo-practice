s = [1,2,3,1]

def containsDuplicates(s):
    numbersSet = set()

    for i in range(len(s)):
        if s[i] not in numbersSet:
            numbersSet.add(s[i])
        else:
            return True
        
    return False

print(containsDuplicates(s))