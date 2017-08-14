def rotate(statement, key):
    rotated = ''
    for i in range(0,len(statement)):
        if statement[i].isalpha():
            numchr = ord(statement[i])
            temp = numchr + key
            if (numchr > 96 - key) and (numchr > 64 and numchr < 91):
                numchr -= 26
                temp = numchr + key
            if (temp > 64 and temp < 91) or (temp > 96 and temp < 123):
                rotated += chr(temp)
            else:
                numchr -= 26
                temp = numchr + key
                rotated += chr(temp)
        else:
            rotated += statement[i]
    return rotated
