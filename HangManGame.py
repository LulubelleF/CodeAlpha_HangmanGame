import random

# Step 1: Define a list of words to choose from
word_list = ['python', 'developer', 'hangman', 'challenge', 'code', 'programming', 'calgary']

# Step 2: Choose a random word from the list
word_to_guess = random.choice(word_list).lower()
word_length = len(word_to_guess)

# Step 3: Initialize the variables
guessed_word = ['_'] * word_length  # Hidden word as underscores
incorrect_guesses = 0
max_incorrect_guesses = 6  # You can change the number of incorrect guesses allowed
guessed_letters = []

# Step 4: Define a function to display the current state of the game
def display_state():
    print("\nCurrent word: " + " ".join(guessed_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")

# Step 5: Main game loop
while incorrect_guesses < max_incorrect_guesses and '_' in guessed_word:
    display_state()
    guess = input("\nGuess a letter: ").lower()

    # Step 6: Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter.")
        continue

    # Step 7: Check if letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Step 8: Check if guessed letter is in the word
    if guess in word_to_guess:
        for idx, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[idx] = letter
        print(f"Good job! '{guess}' is in the word.")
    else:
        incorrect_guesses += 1
        print(f"Sorry, '{guess}' is not in the word.")

# Step 9: End of game messages
if '_' not in guessed_word:
    print("\nCongratulations! You've guessed the word:", word_to_guess)
else:
    print("\nGame over! The word was:", word_to_guess)