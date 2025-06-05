
import random

# This are predefined words
words = ["apple", "train", "river", "house", "plant"]

secret_word = random.choice(words)

# This are Game variables
guessed_letters = []
attempts_left = 6

display_word = ["_" for _ in secret_word]

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Main game loop
while attempts_left > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts_left}")

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try a different one.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!\n")
        attempts_left -= 1

# Game result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Sorry, you're out of attempts. The word was:", secret_word)
