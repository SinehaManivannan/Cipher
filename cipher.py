import random

try:
    import pyperclip
except ImportError:
    pass 

def main():
    while 1:
        print('Enter e for Encrypt Mode or enter d for Decrypt Mode.') 
        answer = input('> ').lower()
        if answer.startswith('d'):
            myMode = 'decrypt'
            break
        elif answer.startswith('e'):
            myMode = 'encrypt'
            break
        print('Enter either e or d.')

    while 1:
            print('What key should we use?')
            if myMode == 'encrypt':
                print('Enter RANDOM to get a random key.')
            answer = input('> ').upper()
            if answer == 'RANDOM':
                theKey = randomKey()
                print('the key is {}'.format(theKey))
                break
            else: 
                if whatKeyIsIt(answer):
                    theKey = answer
                    break
           
    myMessage = input('> ')
    if myMode == 'decrypt':
        translated = decryptMode(theKey, myMessage)
    elif myMode == 'encrypt':
        translated = encryptMode(theKey, myMessage)
    print('The %sed message is:' % (myMode))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('%sed text copied!' % (myMode))
    except:
        pass 

def whatKeyIsIt(key):
    keyList = list(key)
    lettersList = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lettersList.sort()
    keyList.sort()
    if keyList != lettersList:
        print('Error in key or symbol set')
        return False
    return True

def decryptMode(key, message):
    return translate(key, 'decrypt', message)

def encryptMode(key, message):
    return translate(key, 'encrypt', message)

def translate(key, mode, message):
    translated = ''
    firstChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    secondChars = key
    if mode == 'decrypt':
        firstChars, secondChars = secondChars,  firstChars

    for symbol in message:
        if symbol.upper() in    firstChars:
            symIndex =  firstChars.find(symbol.upper())
            if symbol.isupper():
                translated += secondChars[symIndex].upper()

            else:
                 translated += secondChars[symIndex].lower()
        else:
            translated += symbol

    return translated

def randomKey():
    key = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()