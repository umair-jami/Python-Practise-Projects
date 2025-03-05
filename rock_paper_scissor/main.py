# import random

# # Available moves
# moves = ["Rock", "Paper", "Scissor"]

# # User input
# User_Input = input("Enter your move (Rock, Paper, Scissor): ").capitalize()

# # Computer input (random choice)
# Computer_Input = random.choice(moves)

# print(f"Computer chose: {Computer_Input}")

# # Game logic
# if User_Input == Computer_Input:
#     print("Match Tie!")
# elif (User_Input == "Rock" and Computer_Input == "Scissor") or \
#      (User_Input == "Paper" and Computer_Input == "Rock") or \
#      (User_Input == "Scissor" and Computer_Input == "Paper"):
#     print(f"{User_Input} beats {Computer_Input} = You win!")
# elif (Computer_Input == "Rock" and User_Input == "Scissor") or \
#      (Computer_Input == "Paper" and User_Input == "Rock") or \
#      (Computer_Input == "Scissor" and User_Input == "Paper"):
#     print(f"{Computer_Input} beats {User_Input} = Computer wins!")
# else:
#     print("Invalid input! Please enter Rock, Paper, or Scissor.")
import streamlit as st
import random

# Streamlit App Title
st.title("Rock, Paper, Scissors Game 🎮")

# Available moves
moves = ["Rock", "Paper", "Scissor"]

# User selection using radio buttons
User_Input = st.radio("Choose your move:", moves)

# Button to start the game
if st.button("Play"):
    # Computer's random choice
    Computer_Input = random.choice(moves)

    # Display choices
    st.write(f"**You chose:** {User_Input}")
    st.write(f"**Computer chose:** {Computer_Input}")

    # Game logic
    if User_Input == Computer_Input:
        st.info("🎲 It's a Tie!")
    elif (User_Input == "Rock" and Computer_Input == "Scissor") or \
         (User_Input == "Paper" and Computer_Input == "Rock") or \
         (User_Input == "Scissor" and Computer_Input == "Paper"):
        st.success(f"🎉 {User_Input} beats {Computer_Input} - You Win!")
    else:
        st.error(f"😢 {Computer_Input} beats {User_Input} - Computer Wins!")

# Run this script with: `streamlit run script.py`
