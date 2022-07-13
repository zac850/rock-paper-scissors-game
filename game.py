# do you want to play a game? - I'm just going to keep making War Games jokes.
# I got a lot of help from:
# https://realpython.com/python-rock-paper-scissors/
# and from https://www.w3schools.com/python/python_dictionaries.asp 
# and about loops https://www.geeksforgeeks.org/loops-in-python/ and https://www.tutorialspoint.com/python/python_loop_control.htm#
# which of course led to needing a nested loop... https://pynative.com/python-nested-loops/ 
# but I haven't gotten the nested loop work for an invalid choice to bring you back to the choice section of the code...
# and the internet says that using a "goto" code line is really bad form
# I also used random pointers from stackoverflow and other w3schools pages that google showed me when I had specific questions...
import random
import time
import os
# player_name = os.getlogin()    #OTHER Approach below, but I liked this solution better :)
player_name = os.getenv("PLAYER_NAME", default="Player One")
print("Welcome, "+player_name+", to the battle of wits!")
time.sleep(0.5)
while True:
    player_choice=str(input("Rock, Paper, or Scissors? "))
    player_choice = player_choice.lower() #This class note would have saved me a lot of dictonary typing the first time round!
    player_options = ["rock", "r0ck", "r", "paper", "p", "scissors", "scissor", "s",]
    if player_choice not in player_options:
        print("Sorry, that's not a valid choice!")
        break
    computer_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_options)
    # Lookup of winning hands player_choice : computer_choice
    victories = {
        "rock" : "scissors",
        "paper" : "rock",
        "scissors" : "paper",
        "r0ck": "scissors",
        "r": "scissors",
        "p" : "rock",
        "scissors" : "paper",
        "scissor" : "paper",
        "s" : "paper",
    }
    # Lookup ties because otherwise you only tie if you use the same case format... annoying...
    ties = {
        "rock": "rock",
        "r0ck": "rock",
        "r": "rock",
        "scissors" : "scissors",
        "scissor" : "scissors",
        "s" : "scissors",
        "paper" : "paper",
        "p" : "paper",
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

    if ties [player_choice] == computer_choice:
        print(player_name+", you both chose "+player_choice+". It's a tie!")
    elif victories [player_choice] == computer_choice:
        print(player_name+", you chose "+player_choice+" and the computer chose "+computer_choice+". You win!")
    else:
        print(player_name+", you chose "+player_choice+" and the computer chose "+computer_choice+". Sorry, you lose.")
    time.sleep(1)
    play_again = input("That was fun. Would you like to play again? (y/n) ")
    if play_again != "y":
        print("Thanks for playing "+player_name+"!")
        break
