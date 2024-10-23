import random

word_list = ['airplane', 'pizza', 'computer', 'guitar', 'chocolate', 'soccer', 'beach', 'cinema', 'burger', 'mountain', 'sushi', 'basketball']
secret_word = random.choice(word_list)
guessed_letters = []
attempts_left = 6

def reset_game():
    global secret_word, guessed_letters, attempts_left
    secret_word = random.choice(word_list)
    guessed_letters = []
    attempts_left = 6

def play_game(letter):
    global attempts_left

    if letter in guessed_letters:
        return f"You have already used the letter '{letter}'"

    guessed_letters.append(letter)

    display_word = ''.join([l if l in guessed_letters else '_' for l in secret_word])

    if letter not in secret_word:
        attempts_left -= 1
        message = f"Incorrect letter. You have {attempts_left} attempts left."
    else:
        message = f"Correct letter! Current word: {display_word}"

    if '_' not in display_word:

        final_message = f"Congratulations! You guessed the word: {secret_word}"
        reset_game()
        return final_message
    elif attempts_left == 0:
        final_message = f"You lost! The word was: {secret_word}"
        reset_game()
        return final_message

    return message