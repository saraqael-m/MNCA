# MNCA
Contains python program to simulate Multiple Neighborhood Cellular Automata (MNCA). Inspired by [Slackermanz](https://github.com/Slackermanz/VulkanAutomata).

Required **python 3.7** modules: 
- cv2
- numpy
- scipy

My code isn't really fast or clean, I just wanted to show people how beautiful this thing is which [Slackermanz](https://github.com/Slackermanz/VulkanAutomata) discovered, with an easy to use tool to explore the vast world of mnca's.
My youtube video to explain how an mnca works: https://youtu.be/QySHxx_L3G0

The neighborhoods folder contains folders with different rules for the mnca. The names of the files have to be chosen so that they are in the correct order when read by the program. The neighborhood png's have to be black and white (other pixels get rounded to nearest black/white pixel). The *rules.txt* files in each folder aren't read in by the program and they contain the rules for the neighborhoods (value range to kill/revive cells). Those have to be manually pasted into the *nhThresh* variable as seen below. I recommend you to create your own and save them to their corresponding directory if you experiment, so that you don't forget them.

Every desired setting has to be hardcoded in [mncaSim.py](mncaSim.py) after downloading. The following variables are of interest:
- **nhThresh** determines the value ranges for the neighborhoods of the mnca (has as many sublists as neighborhoods, each sublist can contain as many lists as you want, depending on how many conditions you want to use, a condition is formed like this: `[min,max,True/False]`, where min and max is the value range for living cells in the neighborhood and the bool determines wether the cell in the center dies or is born).
- **folder** is the folder with neighborhood images (black and white, each pixel is one cell).
- **start** the dir of the starting configuration for the mnca based on a black and white image (black pixels are living, white are dead; reversed in output).
- **colors** is how living (and dying) cells are colored by different neighborhoods (new colors have to be added if more than 6 neighborhoods are used). Colors are in BGR (blue green red) format, not RGB.
- **m** is the factor by which the output image is scaled.
- **videoname** is the output videos filename.
- **framerate** is the framerate of output video.
- **showImg** is bool if image should be shown while sim is run.
- **trail** is bool if fading trail should be shown behind living cells.
- **colored** is bool if output should be colored.
- **showDying** is bool if dying cells should be shown if colored is true.
- **every** is that only every nth frame in the preview image should be shown.

While the sim is running different buttons can be used to change the sim. Those are listed in the [keys.txt](keys.txt) file.
Run the [mncaSim.py](mncaSim.py) file in the same dir as everything else. Don't try to run it with cmd, use something like [*Sublime Text*](https://www.sublimetext.com/). The start images are saved in the [starts](starts) directory. The videos are saved in the [videos](videos) directory.

https://user-images.githubusercontent.com/80643194/117512823-a7c83780-af90-11eb-903a-9cd41344d056.mp4

https://user-images.githubusercontent.com/80643194/117512906-cfb79b00-af90-11eb-9a0f-7f7210640695.mp4

