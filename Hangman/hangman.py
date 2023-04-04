import selectaword
import board

class Game:
    incorrectGuesses = 0
    correctGuesses = 0
    guessedLetters = []
    word = selectaword.selectWord()

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    def __init__(self):
        self._word = Game.word
        self._length = len(Game.word)
        #has to be a list for it to work
        self._coveredWord = []
        for i in range(0, self._length):
            self._coveredWord.append('_ ')
        #I don't know why this is here but it breaks if it isn't
        self._coveredWord = self._coveredWord
    
    def coveredWordToString(self):
        strWord = ''
        for val in self._coveredWord:
            strWord += val
        return strWord

    def __str__(self):
        #returns the guessed letters and the hangman 
        print(f'Guessed letters: {Game.guessedLetters}')
        print(board.boardStages[Game.incorrectGuesses])
        return self.coveredWordToString() + '\n'

    def guess(self, guess):
        if guess not in Game.alphabet:
            return (f'That is not a valid guess.')
        else:
            if guess in Game.guessedLetters:
                return ('Already guessed that!')
            else:
                Game.guessedLetters.append(guess)
            if guess in self._word:
                listWord = list(Game.word)
                temp = self._word
                count = -1
                indices = []
                for letter in temp:
                    count += 1
                    if letter == guess:
                        indices.append(count)
                for index in indices:
                    self._coveredWord[index] = guess
                    Game.correctGuesses += 1
                return('That is correct')
            else:
                Game.incorrectGuesses += 1
                return ('That is incorrect')
    
                

def runGame():               
    player = Game()
    print(f'The word has {player._length} letters.')
    while True:
        while Game.incorrectGuesses <= 10:
            if Game.incorrectGuesses == 10:
                return(f'Game over, the word was \'{Game.word}\'')
            if Game.correctGuesses == player._length:
                return (f'You win!')
            print(player)
            print(player.guess(input('Please guess a letter:\n')))
            
        
print(runGame())
