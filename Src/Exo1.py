############################################################################
# Partical sesssion : Geometric Transformations on Digital Images          #
#                                                                          #
# Author : Phuc Ngo                                         			   #
#                                                                          #
# Date : August 2023								                       #
#                                                                          #
############################################################################

import cv2 as cv

#Global variable declaration
title_window = "My first program"
img = None
key = 0

###################################
########### Main program ##########
###################################

#Test OpenCV version
print("Your OpenCV version is: " + cv.__version__)

#Get the current directory
cwd = os.getcwd()  
print("Current working directory:", cwd)

#TODO: Read an image given the filename
filename = "../Samples/church.png"
img = cv.imread(FIXME)

#TODO: Create a window
cv.namedWindow(FIXME)

#TODO: Show the image in the created window
cv.imshow(title_window, img)

#TODO: Save the image
cv.imwrite(FIXME)

#Wait for any key then close all the windows
key = cv.waitKey()
cv.destroyAllWindows()

