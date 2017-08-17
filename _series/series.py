def slices(st, l):
    slices = []
    final = []
    finalfinal = []
    if l>len(st) or l == 0:
        raise ValueError()
    for i in range(0,len(st)):
        slices.append(list(st[i:i+l]))
        results = list(map(int, slices[i]))
        final.append(results)
        if len(final[j]) == l:
            finalfinal.append(final[j])
    return finalfinal
