from hangman import Hangman

def main():
    hangman = Hangman()

    print('Can you guess the word.')
    print('Please, Help me from hanging.', '\n')

    # Print Lives.
    print('Lives: ', hangman.lives)

    # Print board.
    print(hangman.board, '\n')

    while hangman.lives and not hangman.win:

        # Get letter.
        letter = input('Enter a letter: ').strip().lower()
        while len(letter) != 1:
            print('Please, enter one letter.')
            letter = input('Enter a letter: ')

        hangman.check_letter(letter)

        # Print Lives.
        print('Lives: ', hangman.lives, '\n')

        # Print guessed letters.
        print('Guessed letters: ', hangman.guessed_letters)

        # Print board.
        print(hangman.board, '\n')

        # Print messages.
        if hangman.lives == 1:
            print('Last chance. Save me, Please.', '\n')
        elif hangman.lives == 0:
            print('X   X', '\n')
            print(f'The word was {hangman.word}.')

        if hangman.win:
            print('Thanks, You saved me from hanging. You\'r my hero.')

if __name__ == '__main__':
    main()
