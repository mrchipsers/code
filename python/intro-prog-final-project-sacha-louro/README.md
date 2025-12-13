python program to simulate the game mastermind in the command line using colour letters (roygbw). has persistent leaderboard with player name and number of guesses required to get correct combination. allows for multiple play throughs.

run the program by running ```project.py``` (```python3 program.py``` in command line, press run in vs code. this is a normal python project with no fancy run requirements). all other files are either called by ```project.py``` or are for testing purpuses only. if you want to run the testing programs just run them as previously described.

This game requires prompt_toolkit for input colouring. it can be installed using pip ```pip install prompt_toolkit``` or conda ```conda install -c https://conda.anaconda.org/conda-forge prompt_toolkit```.

```testMastermind.py``` contains unittests for ```project.py```. used for all functions that dont take user input and return a value.

```testLeaderboard.py``` is used for testing the leaderboard functionality of ```project.py```.

This game has been tested using Linux. I can't guarantee proper functioning of certain colouring features on Windows, but the underlying game should still work.

for the recod I think using gitlab is stupid, I already have a github with all this already.