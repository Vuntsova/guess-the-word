secret_word = "python"
guess = ""
num_guesses = 0
max_guesses = 3
out_of_limit = False

while out_of_limit is False and secret_word != guess:
    guess = input('Guess the secret word: ')
    num_guesses += 1
    if num_guesses == max_guesses:
        out_of_limit = True


if out_of_limit is True:
    print('You Lost')
else:
    print('You Won')
