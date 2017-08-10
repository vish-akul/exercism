import re

def hey(original_statement):

    bob_reply = ''
    statement = original_statement.strip()

    if statement == '' :
        bob_reply = 'Fine. Be that way!'

    elif re.search('(?!^.*[A-Z]{/2,}.*$)^[A-Za-z]*$',statement) is not None:
        bob_reply = 'Whoa, chill out!'

    elif statement[1:] == '?' :
        bob_reply = 'Sure.'

    elif re.search('[a-zA-Z0-9]+',statement) is not None:
        bob_reply =  'Fine. Be that way!'
        
    bob_reply = 'Whatever.'

    return bob_reply
