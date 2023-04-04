
roof =   '-------\n'
middle = '|     |\n'
head =   '|     O\n'
arms =   '|    \'|\'\n'
legs =   '|     ^\n'
base =  '---------'

guess0 = '\n'*5
guess1 = '\n'*4 + base
guess2 = '|\n'*4 + base
guess3 = roof + guess2
guess4 = roof + middle + '|\n'*3 + base
guess5 = roof + middle + head + '|\n'*2 + base
guess6 = roof + middle + head + '|     |\n' + '|\n' + base
guess7 = roof + middle + head + '|    \'|\n' + '|\n' + base
guess8 = roof + middle + head + arms + '|\n' + base
guess9 = roof + middle + head + arms + '|    \'\n' + base
guess10 = roof + middle + head + arms + legs + base

boardStages = [guess0, guess1, guess2, guess3, guess4, guess5, guess6, guess7, guess8, guess9, guess10]



