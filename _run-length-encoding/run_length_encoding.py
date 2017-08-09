def decode(coded):
    letter = ''
    number = ''
    num1 = 0
    ucoded = ''
    if coded.isalpha():
        return coded
    for i in range(0,len(coded)):
        if coded[i].isalpha() or coded[i] == ' ':
            nletter = coded[i]
        elif coded[i+1].isalpha() or coded[i+1] == ' ':
            nletter = coded[i+1]
        if coded[i].isdigit():
            number += coded[i]
            if coded[i+1].isalpha():
                num1 = int(number)
                ucoded += nletter*num1
                number = ''
    return ucoded



def encode(ucoded):
    count = 1
    var1 = ''
    coded = ''
    for i in range(0,len(ucoded)):
        var1 = ucoded[i]
        if (i+1) != len(ucoded) and ucoded[i+1] == var1:
            count += 1
        else:
            if count == 1:
                coded += var1
            else:
                coded += str(count)+var1
                count = 1
    return coded
