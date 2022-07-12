# Welcome

## Prerequisites

* Anaconda 3.7+
* Python 3.7+
* Pip

## Setup

First, download (clone) to your desktop

Then, in your command line, create a virtural enviroment (only need to do this the first time)

 ``` conda create -n rock-paper-scissors python=3.8 ``` 

Next, activate the virtural enviroment you just made

 ``` conda activate rock-paper-scissors ```

Now navigate to the folder the game download exists in

 ``` cd ~/Desktop/rock-paper-scissors-game ```

~~Next step is to install the requirments (there aren't any at this point)~~

~~``` pip install -r requirements.txt ```~~

Lastly, run the game!

``` python game.py ```

## Gameplay

When asked "Rock, Paper, or Scissors?", choose one by typing it in and then hitting return/enter.

Hopefully you win!

After that game, you can choose if you want to play again. If you do, type y and hit return/enter. If not, type n (or literally any other thing in the universe) and hit return/enter.


### User Customization!

Instead of running ``` python game.py ``` as above, instead run:

```PLAYER_NAME="David" python game.py```

Except replace David with your name.