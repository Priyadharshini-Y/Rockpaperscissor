import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image
import random

# Function to simulate AI's move
def ai_move():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(player_move, ai_move):
    if player_move == ai_move:
        return "It's a tie!"
    elif (player_move == 'rock' and ai_move == 'scissors') or \
         (player_move == 'scissors' and ai_move == 'paper') or \
         (player_move == 'paper' and ai_move == 'rock'):
        return "You win!"
    else:
        return "AI wins!"

# Main game loop
while True:
    # Get player's move
    player_move = input("Enter your move (rock, paper, scissors): ").lower()
    
    # Validate player's input
    if player_move not in ['rock', 'paper', 'scissors']:
        print("Invalid move. Please try again.")
        continue
    
    # Simulate AI's move
    ai_choice = ai_move()
    print(f"AI chooses: {ai_choice}")
    
    # Determine the winner
    result = determine_winner(player_move, ai_choice)
    print(result)
    
    # Ask for replay
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")
