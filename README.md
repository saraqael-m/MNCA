# MNCA
Contains python program to simulate Multiple Neighborhood Cellular Automata (MNCA). Inspired by Slackermanz.

Required python 3.7 modules: 
- cv2
- numpy
- scipy

My code isn't really fast or clean, I just wanted to show people how beautiful this thing is which Slackermanz discovered, with an easy to use tool to explore the vast world of mnca's.
My youtube video to explain how a mnca works: WIP

The neighborhoods folder contains folders with different rules for the mnca. The names of the files have to be chosen so that they are in the correct order when read by the program. The neighborhood png's have to be black and white (other pixels get rounded to nearest black/white pixel). The *rules.txt* files in each folder aren't read in by the program and they contain the rules for the neighborhoods (value range to kill/revive cells). Those have to be manually pasted into the *nhThresh* variable as seen below.

Every desired setting has to be hardcoded in "mnca.py" after downloading. The following variables are of interest:
- **nhThresh** determines the value ranges for the neighborhoods of the mnca (has as many sublists as neighborhoods, each sublist can contain as many lists as you want, depending on how many conditions you want to use, a condition is formed like this: `[min,max,True/False]`, where min and max is the value range for living cells in the neighborhood and the bool determines wether the cell in the center dies or is born).
- **folder** is the folder with neighborhood images (black and white, each pixel is one cell).
- **start** the dir of the starting configuration for the mnca based on a black and white image.
- **colors** is how living (and dying) cells by different neighborhoods are colored (colors have to be added if more than 6 neighborhoods are used).
- **m** is the factor by which the output image is scaled.
- **videoname** is the output videos filename.
- **framerate** is the framerate of output video.
- **showImg** is bool if image should be shown while sim is run.
- **trail** is bool if fading trail should be shown behind living cells.
- **colored** is bool if output should be colored.
- **showDying** is bool if dying cells should be shown if colored is true.
- **every** is that only every nth frame in the preview image should be shown.

While the sim is running different buttons can be used to change the sim. Those are listed in the [keys.txt](keys.txt) file.

https://user-images.githubusercontent.com/80643194/117512823-a7c83780-af90-11eb-903a-9cd41344d056.mp4

https://user-images.githubusercontent.com/80643194/117512906-cfb79b00-af90-11eb-9a0f-7f7210640695.mp4

