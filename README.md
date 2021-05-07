# MNCA
Contains python program to simulate Multiple Neighborhood Cellular Automata. Inspired by Slackermanz.

Required python modules: cv2, numpy, scipy

My youtube video to explain how a mnca works: WIP

Every setting has to be hard coded in "mnca.py" after downloading files.
**nhThresh** determines the rules of the mnca.
**folder** is the folder with neighborhood images (black and white, each pixel is one cell).
**start** the dir of the starting configuration for the mnca based on a black and white image.
**colors** is how living (and dying) cells by different neighborhoods are colored (colors have to be added if more than 6 neighborhoods are used).
**m** is the factor by which the output image is scaled.
**videoname** is the output videos filename.
**framerate** is the framerate of output video.
**saveVid** is bool if video should be saved.
**showImg** is bool if image should be shown while sim is run.
**trail** is bool if fading trail should be shown behind living cells.
**colored** is bool if output should be colored.
**showDying** is bool if dying cells should be shown if colored is true.
**every** is that only every nth frame in the preview image should be shown.

While the sim is running different buttons can be used to change the sim. Those are listed in the [keys.txt](keys.txt) file.

https://user-images.githubusercontent.com/80643194/117512823-a7c83780-af90-11eb-903a-9cd41344d056.mp4


https://user-images.githubusercontent.com/80643194/117512906-cfb79b00-af90-11eb-9a0f-7f7210640695.mp4

