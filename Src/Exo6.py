############################################################################
# Partical sesssion : Geometric Transformations on Digital Images          #
#                                                                          #
# Author : Phuc Ngo                                                        #
#                                                                          #
# Date : August 2023                                                       #
#                                                                          #
############################################################################

import cv2 as cv
import numpy as np

title_window1 = "Input binary image"
title_window2 = "Regular binary image"

#Create a black image of size [width, height]
def createBlackImage(width: int, height: int):
    image = np.zeros((height,width,1), np.uint8)
    return image

#Function to read the value of a pixel in image
def getPixelValue(img, row : int, col : int) -> int:
    height,width = img.shape[:2] #Get the dimension of the image
    if(row<height and row>=0 and col<width and col>=0):
        return img[row,col]
    return -1
##Function to set a value to a pixel in image
def setPixelValue(img, row : int, col : int, val : int):
    height,width = img.shape[:2]
    if(row<height and row>=0 and col<width and col>=0):
        img[row,col] = val

#Verify whether the four pixels ([a, b], [c, d] form non well-composed configuration
def isFobidenWellComposedConfigutation(a: int, b: int, c: int, d: int) -> bool:
    if(a!=0 and b==0 and c==0 and d!=0):
        return ((a+b)==255 and (c+d)==255) #As in binary image, white pixel = 255

#Verify whether the given image is well-composed (it does not contain forbidden configuration)
def verifyWellComposedImage(image_in) -> bool:
    #Get dimensions of image
    height, width = image_in.shape[:2]
    #Scan the image and check for the forbidden configuration
    for i in range(height-1):#Row
        for j in range(width-1):#Col
            #TODO: Get the four pixels that form a square of 2x2 (Indication: call getPixelValue for the four pixels (i,j), (i+1, j), (i,j+1), (i+1, j+1))
            a = getPixelValue(image_in, i, j)
            b = getPixelValue(image_in, i+1, j)
            c = getPixelValue(image_in, i, j+1)
            d = getPixelValue(image_in, i+1, j+1)
            #TODO: Call isFobidenWellComposedConfigutation to detect whether the four pixels form a non well-composed configuration
            if(isFobidenWellComposedConfigutation(a,b,c,d)==True):
                return False #Image is not well-composed
    return True #No forbidden configuration detected, image is well-composed

#Create a regular image by upsampling a well-composed binary image
def createRegularImage(image_in):
    #Get dimensions of image
    height, width = image_in.shape[:2]
    #TODO: Create an new image of 2 times bigger than image_in (Indication: call createBlackImage for 2*width x 2*height)
    image_upsampling = FIXME
    #Scan the input image, for each white pixel in image_in, make a square of 2x2 pixel in image_upsampling
    for i in range(height-1):#Row
        for j in range(width-1):#Col
            intensity = getPixelValue(image_in, i, j)
            if intensity == 255:#white pixel
                #TODO: Set the color 255 to the 2x2 pixels in image_upsampling (Indication: call setPixelValue for the four pixels (2*i,2*j), (2*i+1, 2*j), (2*i,2*j+1), (2*i+1, 2*j+1))
                FIXME
                FIXME
                FIXME
                FIXME
    return image_upsampling

###################################
########### Main program ##########
###################################

#Read an image given the filename
#TODO: Change filename here
filename = "../Samples/retina_wc.png"
img = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
#Convert image to a binary image with threshold=125 for example
th_val, img_binary = cv.threshold(img,125,255,cv.THRESH_BINARY)
#Display the input binary image
cv.imshow(title_window1,img_binary)

#TODO: call verifyWellComposedImage to verify the well-composedness of img_binary
is_well_composed = verifyWellComposedImage(img_binary)
#Display the result
if(is_well_composed):
    print("Input image is well-composed, we regularize the image")
    #TODO: call createRegularImage to regularize the input binary well-composed image
    img_regular = FIXME
    #Display the regular image
    cv.imshow(title_window2,img_regular)
    #Save the regular image
    cv.imwrite("../Results/regular_image.png",img_regular)
else:
    print("Sorry, the input image is not well-composed!")

#Wait for any key then close all the windows
key = cv.waitKey()
cv.destroyAllWindows()
