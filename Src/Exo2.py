############################################################################
# Partical sesssion : Geometric Transformations on Digital Images          #
#                                                                          #
# Author : Phuc Ngo                                                        #
#                                                                          #
# Date : August 2023                                                       #
#                                                                          #
############################################################################

import cv2 as cv
import math
import math
import imutils
import numpy as np

#Global variable declaration
title_window = "My first program"
img = None
key = 0

title_slider = "Rotation angle:"
angle_max = 360
angle = 0

#Callback function for the trackbar
def trackbarCallback(angle: int) -> None:
    #TODO: Rotate the image by the angle (in degree) using imutils package (with interpolation)
    rotated = imutils.rotate(img, angle)
    #TODO: Show the rotated image in the window
    cv.imshow(FIXME)
    #TODO: Save the rotated image to: "../Results/rotated_image.png"
    cv.imwrite(FIXME)

###################################
########### Main program ##########
###################################
#Test OpenCV version
print("Your OpenCV version is: " + cv.__version__)

#Get the current directory
cwd = os.getcwd()  
print("Current working directory:", cwd)

#Read an image given the filename
#TODO: Change filename here
filename = "../Samples/retina.png"
img = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)

#Create a window
cv.namedWindow(title_window)

#TODO: Create trackbar associated to the window
cv.createTrackbar(FIXME)
#Call the callback function of trackbar for angle = 0
trackbarCallback(0)

#Wait for any key then close all the windows
key = cv.waitKey()
cv.destroyAllWindows()
