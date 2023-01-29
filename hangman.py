from random_word import RandomWords
random_word = RandomWords()

class Hangman:
    def __init__(self):
        self.word = random_word.get_random_word()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.drawings = ['''
             +---+
             |   |
                 |
                 |
                 |
                 |
         =========''', '''
             +---+
             |   |
             O   |
                 |
                 |
                 |
         =========''', '''
             +---+
             |   |
             O   |
             |   |
                 |
                 |
         =========''', '''
             +---+
             |   |
             O   |
            /|   |
                 |
                 |
         =========''', '''
             +---+
             |   |
             O   |
            /|\  |
                 |
                 |
         =========''', '''
             +---+
             |   |
             O   |
            /|\  |
            /    |
                 |
         =========''', '''
             +---+
             |   |
             O   |
            /|\  |
            / \  |
                 |
         =========''']

    def display_word(self):
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        return display

    def play(self):
        while True:
            print(self.drawings[self.incorrect_guesses])
            print('Incorrect guesses:', self.incorrect_guesses)
            print(self.display_word())
            guess = input('Guess a letter: ').lower()
            if guess in self.guessed_letters:
                print('You already guessed that letter. Try again.')
                continue
            self.guessed_letters.append(guess)
            if guess in self.word:
                print('Correct!')
            else:
                self.incorrect_guesses += 1
                print('Incorrect!')
            if self.incorrect_guesses == 6:
                print(self.drawings[6])
                print('You lost! The word was', self.word)
                break
            if '_' not in self.display_word():
                print('You win! The word was', self.word)
                break


game = Hangman()
game.play()
