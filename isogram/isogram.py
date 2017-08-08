def is_isogram(word):
    lower_word = word.lower()
    default = True
    for i in range(0,len(lower_word)):
        for j in range(0,len(lower_word)):
            if j!=i and lower_word[j] == lower_word[i] and lower_word[j].isalpha():
                default = False
    return default
