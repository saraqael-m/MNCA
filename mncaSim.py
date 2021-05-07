# mnca - multi neighborhood cellular automata
# https://softologyblog.wordpress.com/2018/03/09/multiple-neighborhoods-cellular-automata/

import cv2
import numpy as np
import os
import random
from scipy.ndimage import correlate

# values that determine if cell lives/dies based on number of living cells in neighborhood
nhThresh = [[[0,32,False],[24,46,True]],[[10,25,True]],[[5,22,False]],[[65,75,False],[109,500,False]]]
folder = "neighborhoods/bacteria" # folder with neighborhood images
start = "starts/start100x100.png"
colors = [(52,52,250),(97,240,81),(240,81,84),(232,81,240),(81,213,240),(240,237,81)]
m = 4
videoname = "testmnca.mp4"
framerate = 4
saveVid = True
showImg = True
trail = False
colored = True
showDying = True
every = 1

def draw(event,x,y,flags,param):
    global img, m
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x//m,y//m),15,1,-1)
    elif event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(img,(x//m,y//m),10,1,-1)
        cv2.rectangle(img,(x//m-8,y//m-4),(x//m-1,y//m+4),1,-1)
        cv2.rectangle(img,(x//m+8,y//m-2),(x//m+3,y//m+4),1,-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x//m,y//m),15,0,-1)
        #cv2.rectangle(img,(x//m-8,y//m-4),(x//m+3,y//m+6),1,-1)

def loadNeighborhoods():
	''' load neighborhood shapes based on image files in "neighborhoods" folder
	'''
	global folder
	images = []
	for filename in os.listdir(folder):
	    try:
	        img = 1-(cv2.imread(os.path.join(folder,filename), cv2.IMREAD_GRAYSCALE)/255+.5).astype("uint8")
	        images.append(img)
	    except TypeError:
	    	pass
	return images

def loadStartImg():
	''' load start configuration of living and dead cells based on black and white pixels of "start.png"
	'''
	global img, w, h, start, colored, colImg
	img = 1-(cv2.imread(start, cv2.IMREAD_GRAYSCALE)/255+.5).astype("uint8")
	h, w = img.shape
	colImg = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

def colStep():
	''' one iteration of cellular automata with colors
	'''
	global img, nh, nhThresh, w, h, colImg, showDying
	colImg[:] = (0,0,0)
	nhSums = [correlate(img,n,mode="wrap") for n in nh]
	prevImg = 0
	for n in range(len(nhSums)):
		for t in nhThresh[n]: # check neighborhoods for cells that die / get reincarneted / stay the way they are
			if t[2] == True:
				life = np.logical_and( np.logical_and( nhSums[n] >= t[0], nhSums[n] <= t[1] ), (1-img).astype(bool) ).astype("uint8")
				colImg += (cv2.cvtColor(life,cv2.COLOR_GRAY2RGB)*np.array(colors[n])).astype("uint8")
				img += life # create life
			else:
				death = 1-(np.logical_and( nhSums[n] >= t[0], nhSums[n] <= t[1] )).astype("uint8")
				img *= death # destroy life
				if showDying:
					#colImg *= cv2.cvtColor(death,cv2.COLOR_GRAY2RGB)
					colImg += (cv2.cvtColor(prevImg-img,cv2.COLOR_GRAY2RGB)*(np.array(colors[n])//2)).astype("uint8")
					prevImg = img.copy()
	#colImg[random.randint(0,h-1),random.randint(0,w-1)] = (255,255,255)

def step():
	''' one iteration of cellular automata
	'''
	global img, nh, nhThresh, w, h
	nhSums = [correlate(img,n,mode="wrap") for n in nh]
	for n in range(len(nhSums)):
		for t in nhThresh[n]: # check neighborhoods for cells that die / get reincarneted / stay the way they are
			if t[2] == True:
				img += np.logical_and( np.logical_and( nhSums[n] >= t[0], nhSums[n] <= t[1] ), (1-img).astype(bool) ).astype("uint8") # create life
			else:
				img *= 1-(np.logical_and( nhSums[n] >= t[0], nhSums[n] <= t[1] )).astype("uint8") # destroy life

cv2.namedWindow('mnca')
cv2.setMouseCallback('mnca',draw)
nh = loadNeighborhoods() # neighborhoods from images
loadStartImg()
imgArr = []
c = -1
prevImg = 0
while True:
        c += 1
        if colored:
        	colStep()
        	newImg = np.repeat(np.repeat(colImg,m,axis=0),m,axis=1)
        else:
	        step()
	        newImg = np.repeat(np.repeat(img*255,m,axis=0),m,axis=1)
        if trail:
                if c > 0:
                        newImg = ((prevImg*((255-newImg)//255))/1.1).astype("uint8")+newImg
                prevImg = newImg.copy()
        if showImg and c//every == c/every:
                cv2.imshow("mnca",newImg)
        if saveVid:
                imgArr.append(newImg.copy())
        k = cv2.waitKey(1)
        if k == ord("v"): # change neighborhood thresholds
                print("Previous Vals:",nhThresh)
                f = input("New Neighborhood Threshold Vals: ")
                if str(f) != "":
                        exec("nhThresh = "+f)
        elif k == ord("u"): # change neighborhoods (update from files)
                print("Previous Folder:",folder)
                if k == ord("u"):
                        f = input("New Neighborhood Folder: ")
                        if str(f) != "":
                                folder = f
                        print("Previous Vals:",nhThresh)
                        f = input("New Neighborhood Threshold Vals: ")
                        if str(f) != "":
                                exec("nhThresh = "+f)
                nh = loadNeighborhoods()
        elif k == ord("a"):
            nh = loadNeighborhoods()
        elif k == ord("r"):
            loadStartImg()
            imgArr = []
        elif k == ord("l"):
            print("Previous Image:",start)
            start = input("New Image Dir: ")
            loadStartImg()
            imgArr = []
        elif k == ord("p"): # pause the sim
                print("paused")
                cv2.waitKey(0)
                print("playing")
        elif k == 27: # stop the sim
                saveVid = False
                break
        elif k == ord("x"): # stop the sim and save vid
                saveVid = True
                break

if saveVid:
	_, _, filenames = next(os.walk("C:\\Users\\maxim\\Desktop\\rem\\programming\\python\\sim\\cellularAutomata\\mnca"))
	while videoname in filenames:
		videoname = "saved_"+videoname
	out = cv2.VideoWriter(videoname, cv2.VideoWriter_fourcc(*'mp4v'), framerate, (w*m,h*m), colored)
	for i in range(len(imgArr)):
	    out.write(imgArr[i])
	cv2.destroyAllWindows()
	out.release()
cv2.destroyAllWindows()
