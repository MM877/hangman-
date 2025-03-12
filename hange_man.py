import random  # Import the random module to randomly select a word from the list

# Hangman stages (drawings)
hangman_stages = [
    """
      ------
      |    |
      |    
      |    
      |    
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |    
      |    
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |    |
      |    
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |    
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |    
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |    
    =====
    """  # Final stage (loss)
]

word = ['camel', 'lion', 'joy', 'tiger', 'zebra', 'cheetah']  # List of possible words
choosen_word = random.choice(word)  # Randomly pick one word from the list

# Create a placeholder with underscores for each letter in the chosen word
placeholder = ['_' for _ in choosen_word]  # This creates a list of "_" with the same length as the word
word_length = len(choosen_word)  # Get the length of the chosen word

print(" ".join(placeholder))  # Print the placeholder as a string with spaces between underscores

game_over = False  # Boolean flag to track if the game is over
correct_letters = []  # List to store correct guessed letters (not used in this version)
attempts = 0  # Track incorrect guesses

while not game_over:  # Keep running the game loop until the player wins
    guess = input("Guess a letter: ").lower()  # Ask the player to guess a letter and convert it to lowercase

    # Flag to track if the guessed letter is in the word
    correct_guess = False

    for position in range(word_length):  # Loop through each letter in the chosen word
        if choosen_word[position] == guess:  # If the guessed letter matches the current letter in the word
            placeholder[position] = guess  # Replace the "_" in the placeholder with the correct letter
            correct_guess = True  # Set the flag to True since the guess was correct

    if not correct_guess:  # If the guess was wrong, increase the attempts
        attempts += 1
        print(hangman_stages[attempts])  # Print the corresponding Hangman stage

    print(" ".join(placeholder))  # Print the updated placeholder with guessed letters

    # Check if the player has guessed all letters (i.e., no underscores left)
    if "_" not in placeholder:
        game_over = True  # Set game_over to True to stop the loop
        print("You win!")  # Display a winning message

    # Check if the player has lost
    if attempts == len(hangman_stages) - 1:
        game_over = True
        print("You lost! The word was:", choosen_word)  # Show the correct word
