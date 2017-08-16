def slices(st, l):
    slices = []
    final = []
    finalfinal = []
    if l>len(st) or l == 0:
        raise ValueError()
    for i in range(0,len(st)):
        slices.append(list(st[i:i+l]))
    for j in range(0,len(slices)):
        results = list(map(int, slices[j]))
        final.append(results)
    for k in range(0,len(final)):
        if len(final[k]) == l:
            finalfinal.append(final[k])
    return finalfinal
