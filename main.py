import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image

# Function to build the CNN model
def build_model(input_shape):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(3, activation='softmax')  # 3 classes: rock, paper, scissors
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Load the trained CNN model
model = build_model(input_shape=(150, 150, 3))
model.load_weights('rps_model.h5')

# Function to predict user's choice using the CNN model
def predict_user_choice(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize pixel values
    prediction = model.predict(img_array)
    choices = ['rock', 'paper', 'scissors']
    user_choice = choices[np.argmax(prediction)]
    return user_choice

# Play Rock, Paper, Scissors with CNN
def play_rps_with_cnn():
    while True:
        user_img_path = input("Enter path to your image (rock, paper, or scissors): ")
        user_choice = predict_user_choice(user_img_path)

        computer_choice = np.random.choice(["rock", "paper", "scissors"])

        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
             print("You lose!")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break

# Start the game
play_rps_with_cnn()
