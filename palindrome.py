s = "shivam"
list1 = []
list2 = []

def checkPalindrome(s):

    for j in range(len(s)):
        list1.append(s[j])

    for i in range(len(s) - 1, -1, -1):
        list2.append(s[i])

    if list1 == list2:
        return True
    else:
        return False
        
print(checkPalindrome(s))