def detect_anagrams(s,candidates):
    newlist = []
    for i in range(0,len(candidates)):
        if set(s.lower()) == set(candidates[i].lower()) and s.lower() != candidates[i].lower():
            #if set(s).issubset(set(candidates[i])) or set(s).issuperset(set(candidates[i])):
            #    pass
            if candidates[i] in newlist:
                pass
            else:
                newlist.append(candidates[i])
    return newlist
