# Welcome

## Prerequisites
* Anaconda 3.7+
* Python 3.8+

## Setup
First, download (clone) to your desktop

Then, in your command line (e.g. Terminal), create a virtural enviroment (you only need to do this the first time):

 ```sh
 conda create -n rock-paper-scissors python=3.8
 ``` 

Next, activate the virtural enviroment you just made:

 ```sh
 conda activate rock-paper-scissors
 ```

Now navigate to the folder the game download exists in (should be your desktop, if you followed step 1):

 ```sh
 cd ~/Desktop/rock-paper-scissors-game
 ```

Lastly, run the game:

```sh
python game.py
```

## Gameplay

When asked "Rock, Paper, or Scissors?", choose one by typing it in and then hitting return/enter.

Hopefully you win!

After that game, you can choose if you want to play again. If you do, type y and hit return/enter. If not, type n and hit return/enter.


## User Customization!

Instead of running ```python game.py``` as above, instead run:

```sh
PLAYER_NAME="David" python game.py
```

Except replace David with your name (your name needs to be in quotes, like ```"David"``` above)