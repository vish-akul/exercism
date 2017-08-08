import string

def word_count(phrase):
    exclude = set(string.punctuation)
    exclude.remove('_')
    exclude.remove(',')
    phrase = ''.join(ch for ch in phrase if ch not in exclude)
    phrase = phrase.lower()
    word_list = []
    if '_' or ',' in phrase:
        for sp in '_,"':
            phrase = phrase.replace(sp, ' ')
        word_list = phrase.split()
    else:
        word_list = phrase.split()
    final_dict = {}
    for i in range(0,len(word_list)):
        word = word_list[i]
        repeats = word_list.count(word)
        final_dict[word] = repeats
    return final_dict
