#!/usr/bin/env python
# coding: utf-8

# In[9]:


print("Welcome to Coin Toss")
name = input("Im Mac. 👋 What is your name? ")
print('Hello', name, "! Here are the rules of the game.\nThe Coin will randomly be tossed and you will input you guess \nThen you will either win or loose and you can replay!")


# In[27]:


import random
while True:
    play_status = input("Do you want to play? (yes/no) ")
    if play_status.lower() == "yes":
        #this is where we play the gameye
        options = ["heads","tails"]
        toss = random.choice(options)
        player_coin = input("Pick heads or tails. ")
        player_coin = player_coin.lower()
        if player_coin == "heads" or player_coin == "tails":
            if player_coin == toss:
                print("You Won! 🥳🥳")
                print("It was", toss)
            else:
                print("You're a loser 😵😵")
                print("It was", toss)
        else:
            print ("Choose heads or tails.")
    else:
        break
        


# In[ ]:




