############################################################################
# Partical sesssion : Geometric Transformations on Digital Images          #
#                                                                          #
# Author : Phuc Ngo                                                        #
#                                                                          #
# Date : August 2023                                                       #
#                                                                          #
############################################################################

import math
import cv2 as cv
import numpy as np

#Global variable declaration
title_window1 = "Forward rotation"
title_window2 = "Backward rotation"

title_slider = "Rotation angle:"
angle_max = 360
angle1 = 0
angle2 = 0

img = None

#Class of image point in Z2
class ImagePoint:
    row: None  # int
    col: None  # int

    def __init__(self, row_, col_):
        self.row = row_
        self.col = col_

    def __copy__(self):
        return ImagePoint(self.row, self.col)

    def printImagePoint(self):
        print("ImagePoint:(", self.row, ", ", self.col, ")")

#Class of real point in R2
class RealPoint:
    x: None  # int
    y: None  # int

    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

    def __copy__(self):
        return RealPoint(self.x, self.y)

    def digitizeRealPoint(self) -> ImagePoint:
        return ImagePoint(int(np.round(self.y)), int(np.round(self.x)))

    def printRealPoint(self):
        print("RealPoint:(", self.x, ", ", self.y, ")")

#Class of (forward and backward) rotation for digital image
class rotation:
    angle: None  # float, rotation angle in degree
    center : None # center of rotation
    rotMatrix : None #Rotation matrix from given angle (in degree)

    def __init__(self, angle_):
        self.angle = angle_
        self.center = RealPoint(0,0)
        convert_angle = self.angle*math.pi/180 #Convert angle from degrees to rads
        cos = math.cos(convert_angle)
        sin = math.sin(convert_angle)
        self.rotMatrix = np.array([[cos, -sin], [sin, cos]])  #Rotation matrix an array of floats

    def __init__(self, angle_, center_):
        self.angle = angle_
        self.center = center_
        convert_angle = self.angle*math.pi/180
        cos = math.cos(convert_angle)
        sin = math.sin(convert_angle)
        self.rotMatrix = np.array([[cos, -sin], [sin, cos]])  #Rotation matrix an array of floats

    def getRotationMatrix(self):
        return self.rotMatrix

    def getInverseRotationMatrix(self):
        #TODO: initize the invers rotation matrix with -angle
        convert_angle = self.angle*math.pi/180
        cos = math.cos(convert_angle)
        sin = math.sin(convert_angle)
        #TODO: initize the rotation matrix from the cos and sin (Indication: do similarly to the previous function)
        invRotMatrix = np.array([[cos, sin], [-sin, cos]])  #Inverse Rotation matrix an array of floats
        return invRotMatrix

    def forwardRotation(self, p : RealPoint) -> RealPoint:
        rp = np.array([p.x-self.center.x,p.y-self.center.y]) #Convert the point into an array for multiplication matrix
        rotP = self.rotMatrix.dot(rp) #Apply a multiplication matrix between the point and the rotation matrix
        return RealPoint(rotP[0]+self.center.x, rotP[1]+self.center.y)

    def digitizedForwardRotation(self, p : RealPoint) -> ImagePoint:
        #TODO: apply forwardRotation function on point p
        rp = self.forwardRotation(p)
        #TODO: call digitizeRealPoint function for rp to obtain a digitized point
        dp = rp.digitizeRealPoint()
        return dp

    def backwardRotation(self, p : RealPoint) -> RealPoint:
        rp = np.array([p.x-self.center.x,p.y-self.center.y])
        #TODO: call getInverseRotationMatrix function to get the inverser rotation matrix
        rotMatrix = self.getInverseRotationMatrix()
        #TODO: apply multiplication matrix between the point pr and the rotation matrix rotMatrix (Indication: do similarly to the forwardRotation function)
        rotP = rotMatrix.dot(rp)
        return RealPoint(rotP[0]+self.center.x, rotP[1]+self.center.y)

    def digitizedBackwardRotation(self, p : RealPoint) -> ImagePoint:
        #TODO: apply backardRotation function on point p
        rp = self.backwardRotation(p)
        #TODO: call digitizeRealPoint function for rp to obtain a digitized point
        return rp.digitizeRealPoint()

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

###################################
######## Optional: Trackbar #######
###################################
''' Uncomment this if you want to run this part of the code
#Callback function for the trackbar of forward rotation
def trackbarCallback1(angle: int) -> None:
    #TODO: Rotate the image by the angle (in degree) using imutils package (with interpolation)
    rotated = forwardRotationImage(FIXME)
    #TODO: Show the rotated image in the window 1
    cv.imshow(FIXME)
    #TODO: Save the rotated image
    cv.imwrite(FIXME)

#Callback function for the trackbar of backward rotation
def trackbarCallback2(angle: int) -> None:
    #TODO: Rotate the image by the angle (in degree) using imutils package (with interpolation)
    rotated = backwardRotationImage(FIXME)
    #TODO: Show the rotated image in the window 2
    cv.imshow(FIXME)
    #TODO: Save the rotated image
    cv.imwrite(FIXME)

'''

#Create a black image of size [width, height]
def createBlackImage(width: int, height: int):
    image = np.zeros((height,width,1), np.uint8)
    return image

#Forward rotation of a given image
def forwardRotationImage(image_in, theta):
    #Get dimensions of image
    height, width = image_in.shape[:2]
    #Create a black image to store the transformed result
    image_out = createBlackImage(width,height)
    #TODO: Create an objet of rotation class for the rotation angle theta with center at RealPoint(width/2,height/2)
    rot = FIXME
    #Realized the digitized forward rotation
    for i in range(width):#Col - x
        for j in range(height):#Row - y
            #Get the point in image
            p = RealPoint(i, j)
            #TODO: Call digitizedForwardRotation to transform the point
            rp = FIXME
            #Get the pixel value for the point (i,j) in the image
            v = getPixelValue(image_in, j, i)
            #Set the obtained value to the transformed point
            setPixelValue(image_out, rp.row, rp.col, v)
    #Return the transformed result
    return image_out

#Backward rotation of a given image
def backwardRotationImage(image_in, theta):
    #Get dimensions of image
    height, width = image_in.shape[:2]
    #Create a black image to store the transformed result
    image_out = createBlackImage(width,height)
    #TODO: Create an objet of rotation class for the rotation angle theta with center at RealPoint(width/2,height/2)
    rot = FIXME
    #Realized the digitized backward rotation
    for i in range(width):#Col - x
        for j in range(height):#Row - y
            #Get the point in image
            p = RealPoint(i, j)
            #TODO: call digitizedBackwardRotation to transform the point
            rp = FIXME
            #Get the pixel value for the point (i,j) in the image
            v = getPixelValue(image_in, rp.row, rp.col)
            if(v!=-1): #If the pixel is in the image, then set the value to the point (i,j)
                setPixelValue(image_out, j, i, v)
    #Return the transformed result
    return image_out

###################################
########### Main program ##########
###################################

#Read an image given the filename
#TODO: Change filename here
filename = "../Samples/church.png"
img = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)

#Call forwardRotationImage on the input image img
angle = 45
forward_rot_image = forwardRotationImage(img, angle)
#Display the result
cv.imshow(title_window1, forward_rot_image)
#Save the result
cv.imwrite("../Results/forward_rotation_image.png", forward_rot_image)

#Call backwardRotationImage on the input image img
backward_rot_image = backwardRotationImage(img, angle)
#Display the result
cv.imshow(title_window2, backward_rot_image)
#Save the result
cv.imwrite("../Results/backward_rotation_image.png", backward_rot_image)

###################################
######## Optional: Trackbar #######
###################################
''' Uncomment this if you want to run this part of the code
#Create a window
#cv.namedWindow(title_window1)
#cv.namedWindow(title_window1)

#TODO: Create trackbar associated to the window
cv.createTrackbar(title_slider, title_window1, angle1, angle_max, trackbarCallback1)
#Call the callback function of trackbar for angle = 45
trackbarCallback1(45)

cv.createTrackbar(title_slider, title_window2, angle2, angle_max, trackbarCallback2)
#Call the callback function of trackbar for angle = 45
trackbarCallback2(45)
'''

#Wait for any key then close all the windows
key = cv.waitKey()
cv.destroyAllWindows()
