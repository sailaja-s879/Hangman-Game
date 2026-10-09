import random

words = ["python", "computer", "programming", "developer", "keyboard"]
word = random.choice(words)
guessed_letters = []
max_attempts = 6
incorrect_guesses = 0

print("WELCOME TO HANGMAN")
print("Guess the word one letter at a time!")

while incorrect_guesses < max_attempts:
    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter.")
        continue

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Incorrect guess!")

if incorrect_guesses == max_attempts:
    print("Game over! The word was:", word)
