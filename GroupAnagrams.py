s = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    groups = {}

    for word in strs:
        key = sorted(word) 
        key = "".join(sorted(word))

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
            
    return groups.values()
groupAnagrams(s)