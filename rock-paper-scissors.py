#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
options = ["rock","paper","scissors"]
game_end = False

print("Welcome to Rock, Paper, Scissors")
name = input("Im Mac. 👋 What is your name? ")
print('Hello', name, "! Here are the rules of the game.")
print("""You will be able to choose rock, paper or scissors and the computer will choose rock, paper or scissors.
Rock defeats scissors.
Scissors cuts paper.
Paper covers rock.
If both are the same then there is a tie.""")

while game_end == False:
    comp_choice = random.choice(options)
    user_choice = input("Enter your choice. (rock, paper, scissors) ")
    if user_choice == comp_choice:
        print("That was a tie.")
    elif user_choice == "rock":
        if comp_choice == "paper":
            print("You lost! Paper covers rock.")
        elif comp_choice == "scissors":
            print("You won! Rock defeats scissors.")
    elif user_choice == "paper":
        if comp_choice == "scissors":
            print("You lost! Scissors cuts paper.")
        elif comp_choice == "rock":
            print("You won! Paper covers rock.")
    elif user_choice == "scissors":
        if comp_choice == "rock":
            print("You lost! Rock defeats scissors.")
        elif comp_choice == "paper":
            print("You won! Scissors cuts paper.")
    else:
        print("Invalid input. Please try again.")
    play_again = input("Would you like to play again? (yes/no) ")
    if play_again.lower == "no":
        break

