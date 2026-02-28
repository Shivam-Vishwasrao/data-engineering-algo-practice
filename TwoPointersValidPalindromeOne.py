# s = "racecar"
# s = "hello"
s = "abba"

def TwoPointerPalindrome(s):
    rightPointer = len(s) - 1
    leftPointer = 0
    while leftPointer < rightPointer:
        if s[leftPointer] == s[rightPointer]:
            leftPointer += 1
            rightPointer -= 1
        else:
            return False
    return True

print(TwoPointerPalindrome(s))