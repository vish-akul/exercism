def distance(original_strand,new_strand):
    hamming = 0
    if len(original_strand) != len(new_strand):
        raise ValueError()
    for i in range(0,len(original_strand)):
        if original_strand[i] != new_strand[i]:
            hamming += 1
    return hamming
