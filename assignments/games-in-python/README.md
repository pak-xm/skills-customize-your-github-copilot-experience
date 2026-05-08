
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, and conditionals. By the end of this assignment, you will create a playable terminal game that tracks guesses and determines win or loss outcomes.

## 📝 Tasks

### 🛠️ Create the Game Setup

#### Description
Set up the core game data and starting state before the game loop begins.

#### Requirements
Completed program should:

- Store a predefined list of possible words.
- Randomly select one word as the hidden target word.
- Set a starting number of incorrect guesses allowed.
- Initialize data structures to track guessed letters and game progress.


### 🛠️ Build the Gameplay Loop

#### Description
Implement the main game loop that accepts guesses, updates progress, and ends with a clear result.

#### Requirements
Completed program should:

- Accept one letter guess at a time from the user.
- Display the current word progress in underscore format for unguessed letters.
- Decrease remaining attempts only for incorrect guesses.
- End the game when the full word is guessed or no attempts remain.
- Display a clear win or lose message at the end of the game.
