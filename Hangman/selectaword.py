from random import randint
def selectWord():
    #opens list of words, where the words are stored as a csv
    with open('dictionary.txt', 'r') as file:
        f = file.readlines()
        f = f[0].strip('\n')
        f = f.split(' ')
    dictLength = len(f)
    #picks and returns a random word from the list
    return f[randint(0, dictLength-1)]
