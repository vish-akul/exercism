def to_rna(dna):
    dna_set = 'GCTA'
    new_dna = ''
    for i in range(0,len(dna)):
        if dna[i] not in dna_set:
            return ''
        if dna[i] == 'G':
            new_dna += 'C'
        elif dna[i] == 'C':
            new_dna += 'G'
        elif dna[i] == 'T':
            new_dna += 'A'
        elif dna[i] == 'A':
            new_dna += 'U'
        else:
            new_dna = ''
    return new_dna
