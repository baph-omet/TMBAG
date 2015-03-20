# TMBAG
This Might Be A Game - A text-based RPG written in Python 3.4.1

This game is a side-project that I'm working on to help myself learn Python and some of the basics of game programming. As such, it's a work-in-progress. The game is not yet playable, as I'm working on a lot of the behind-the-scenes stuff at the moment (battle engine, for starters). Once I have all that stuff finished, writing the story should be pretty straightforward.

## How to Play
### Running the game
This game is run exclusively in the Python console. Make sure you're using at least Python 3.

#### If you DON'T have Python installed
If you don't have Python installed on your computer (you would know if you did), you can play this game from any online Python interpreter that supports Python 3 (here's one: http://www.tutorialspoint.com/execute_python3_online.php). Just copy all the python files (`*.py`) into the file list on the left side of the page and execute `main.py`. It's that simple!

Alternatively, you can download and install Python 3 from http://python.org and then skip to the next section.

#### If you DO have Python installed
If you do have Python installed on your computer, download all the files and extract them into the same folder. Then there are a few ways to start the game:
##### Easy Way
Just double-click on the file `main.py`. This will open a new command prompt window containing the game. You may want to resize the window so you can see past lines of text.
##### Slightly Less Easy Way
Open the file `start.bat` with a plaintext editor (Notepad++ is recommended) and edit the filepath on the first line to use the filepath to the file `main.py` game's folder (i.e. `C:\Users\Joe\Downloads\TMBAG\main.py`), then just run the file `start.bat` to play the game from a command prompt, or drag it into an already open command prompt window.
##### The IDLE Way
Alternatively, you can open the file `main.py` in IDLE and hit F5 to start the shell, although this is a bit slower.

### Playing the game
Throughout the game, you interact via supplying text input for various prompts. Prompts are case-insensitive. For most prompts, you can enter `menu` to access the in-game menu to see stats, rename your character, and more. Hit the ENTER key to advance text in story sections.

## Planned Additions
(?) - Possible additions
- ~~Special moves~~
- Shops
- ~~Inventory system~~
- Random encounters (?)
- Some sort of visual component (?)
- .exe version for non-python users

## Issues
Feel free to submit any issues you have with the game on github. I appreciate it!
If you're getting an unhandled Python error, please copy the entire error message, including the stack trace, into the issue report.
If you're having issues running the `start.bat` file, make sure you put in the correct filepath after the `python` statement on the first line. If your filepath contains spaces, enclose it in quotations.

## Pull Requests
I'm not really looking for help developing this game, however if you see any errors or just stupid coding decisions on my part, feel free to submit a pull request and I'll take a look at it.
