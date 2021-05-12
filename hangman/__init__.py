import json
from random import choice, gauss

class Hangman:

    def __init__(self):
        self.word = Hangman.get_word()
        self.empty_word = ['_' for i in range(0, len(self.word))]
        self.lives = 3
        self._guessed_letters = []

    @property
    def board(self) -> str:
        '''Print Hangman board'''
        board = ' '.join(self.empty_word)
        board = board.capitalize()

        return board

    @property
    def guessed_letters(self):
        letters = ' '.join(self._guessed_letters)
        return letters

    @guessed_letters.setter
    def guessed_letters(self, letter) -> bool:
        if letter in self._guessed_letters:
            return

        self._guessed_letters.append(letter)

    @property
    def win(self) -> bool:
        '''Checks if Hangman is saved'''
        guessed_word = ''.join(self.empty_word)

        if self.word == guessed_word:
            return True
        
        return False

    @classmethod
    def get_word(cls) -> str:
        '''Retrive random word'''
        with open('data/words.json') as words:
            word = choice(json.load(words))

        return word

    def check_letter(self, letter) -> None:
        '''Checks if the letter existed in the word'''
        letter_existed = False

        if letter in self._guessed_letters:
            print(f'You typed this letter before.')
            return
        
        self.guessed_letters = letter

        for i in range(0, len(self.word)):
            if self.word[i] == letter:
                self.empty_word[i] = letter
                letter_existed = True

        if not letter_existed:
            self.lives -= 1
        

