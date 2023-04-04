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

def findIndices(list_of_elems, element):
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = list_of_elems.index(element, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

print(selectWord())