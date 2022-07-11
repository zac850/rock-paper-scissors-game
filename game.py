# do you want to play a game?
# I got a lot of help from
# https://realpython.com/python-rock-paper-scissors/
# and from https://www.w3schools.com/python/python_dictionaries.asp 
# and about loops https://www.geeksforgeeks.org/loops-in-python/
# and random pointers from stackoverflow and google and other w3schools pages...
import random
import time
import os
from tkinter import END
player_name = os.getlogin()
print("Welcome",player_name,"to the battle of wits!")
while True:
    player_choice=str(input("Rock, Paper, or Scissors?"))
    player_options = ["Rock", "Paper", "Scissors", "rock", "ROCK", "r0ck", "r", "PAPER", "paper", "p", "SCISSORS", "scissors", "scissor", "s"]
#    if player_choice not in player_options:
#        print("Sorry, that's not a valid choice!")
#    else:
#        continue
    computer_options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_options)
    # Lookup of winning hands player_choice : computer_choice
    victories = {
        "Rock" : "Scissors",
        "Paper" : "Rock",
        "Scissors" : "Paper",
        "rock" : "Scissors",
        "ROCK": "Scissors",
        "r0ck": "Scissors",
        "r": "Scissors",
        "PAPER" : "Rock",
        "paper" : "Rock",
        "p" : "Rock",
        "SCISSORS" : "Paper",
        "scissors" : "Paper",
        "scissor" : "Paper",
        "s" : "Paper",
    }

    # From https://python-forum.io/thread-26430.html
    print("   Rock")
    time.sleep(0.2)
    print("   Paper")
    time.sleep(0.3)
    print("   Scissors")
    time.sleep(0.4)
    print("   Shoot!")
    time.sleep(0.5)

    if player_choice == computer_choice:
        print(player_name,"you both chose ",player_choice,". It's a tie!")
    elif victories [player_choice] == computer_choice:
        print(player_name,"you chose",player_choice,"and the computer chose ",computer_choice,". You win!")
    else:
        print(player_name,"you chose",player_choice,"and the computer chose ",computer_choice,". Sorry, you loose.")
    time.sleep(1)
    play_again = input("That was fun. Would you like to play again (y/n)?")
    if play_again != "y" or "yes":
        break