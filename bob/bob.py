import re

def hey(statement):
    statement = statement.strip()
    if statement == '':
        return 'Fine. Be that way!'
    elif statement.isupper():
        return 'Whoa, chill out!'
    elif '?' == statement[-1]:
        return 'Sure.'
    elif not re.search('[a-zA-Z0-9]+',statement):
        return 'Fine. Be that way!'
    return 'Whatever.'
