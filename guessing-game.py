#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


print("Welcome to the guessing game!")
name = input("Hello, I'm Mac. What's your name? ")

print("Hi", name + "! Nice to meet you!")


# In[3]:


print("Here are the rules of the game: \nThe goal is the guess a random number between 1 and 20 in 5 guesses")


# In[ ]:


restart = input("Would you like to play? (yes/no) ")
while restart == "yes":
    attempts = 5
    game_end = False

    number = random.randint (1,20)

    while attempts > 0 and game_end == False:
        guess = input("What's your guess? ")


        #check if number is non-numeric string
        check1 = False
        if guess.lstrip('-').isnumeric():
            check1 = True
        else:
            check1 = False


        #check if input is a float and convert into integer
        check3 = False
        if check1 == False:    
            if guess.rstrip('0')[-1] == '.':
                check3 = True
                check1 = True
            else:
                check3 = False
                print("Please input an whole integer.")
        else:
            check3 = True


        #check if input is in range
        check4 = False
        if check1 == True:
            if float(guess) in range (1, 21):
                check4 = True
            else:
                check4 = False
                print("Please input a guess in the range of 1 and 20.")
        else:
            check4 = False


        if check1 == True and check3 == True and check4 == True:
            guess = float(guess)
            attempts = attempts - 1
            if guess == number:
                print("That is the correct answer!")
                game_end = True
                restart = input("Would you like to play? (yes/no) ")
            elif guess > number:
                print ("Your guess is too high!")
                print("You have", attempts, "attempts left.")
            else:
                print("Your guess is too low!")
                print("You have", attempts, "attempts left.")
        else:
            print("Input is invalid")


        if attempts == 0 and guess is not number:
            print("You lost! \nThe number I was thinking of was:", number)
            restart = input("Would you like to play? (yes/no) ")

