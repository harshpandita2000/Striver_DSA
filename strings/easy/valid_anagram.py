def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    counts = {}

    for element in s1:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    for element in s2:
        if element in counts:
            counts[element] -= 1
        else:
            counts[element] = 1
    
    for element,counts in counts.items():
        if counts != 0:
            return False
    return True

s1 = "anagram"
s2 = "nagaram"
print(anagram(s1,s2))


    
    

   