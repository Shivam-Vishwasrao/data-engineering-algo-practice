s = "abcabcbb"
#s = 'abba'
# Since we are checking for duplicates in a substring, we can use sets. We are not keeping track of
# exact number of duplicates, so, we don't need hashmap level of complexcity here. We can just keep 
# a running total of what the max length of the unique substring is every time the window moves.
# 

def longestSubString(s):
    # Creating a set to hold unique characters from string s
    charSet = set()
    length = 0
    max_length = 0
    left = 0
    # Let's start by iterating over the string 's'. 
    # (1) if unique character is found, add it to the set + increment length
    # (2) if duplicate found -> condition break -> left window moves
    #      we delete element at index 0 (left) then move left up by 1, we repete the removing 
    #      till we are back to having a set of unique characters in the set. then we add the new 
    #       element to the set and count the length again. 
    for right in range(len(s)):
        if s[right] not in charSet:
            charSet.add(s[right])
            length += 1
            max_length = max(length, max_length)
        else:
            while s[right] in charSet:
                charSet.remove(s[left])
                length -= 1
                left += 1
            
            charSet.add(s[right])
            max_length = max(max_length, right - left + 1)
    
    return max_length

print(longestSubString(s))
