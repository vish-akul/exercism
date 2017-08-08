def is_pangram(word):
    word = word.lower()
    the_alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_word = ""
    for char in word:
        if char in the_alphabet:
            new_word += char
    if set(the_alphabet) == set(new_word):
        return True
    else:
        return False
