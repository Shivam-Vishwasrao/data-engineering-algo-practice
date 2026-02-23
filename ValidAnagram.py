s = "anagram"
t = "nagaram"

def validAnagram(str1, str2):
    # Edge Case validation
    if len(str1) != len(str2):
        return False
    else:
        count = {}

        # count characters in str1
        for c in str1:
            count[c] = count.get(c,0) + 1

        # substract using str2
        for c in str2:
            if c not in count:
                return False
            
            count[c] -+ 1

            if count[c] < 0:
                return False
        return True
    
validAnagram(s, t)