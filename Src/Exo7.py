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
title_window1 = "Backward rotation"
title_window2 = "Connected component labelling"

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
        #Initize the rotation matrix from the cos and sin
        self.rotMatrix = np.array([[cos, -sin], [sin, cos]])  #Rotation matrix an array of floats

    def getRotationMatrix(self):
        return self.rotMatrix

    def getInverseRotationMatrix(self):
        #Initize the invers rotation matrix with -angle
        convert_angle = self.angle*math.pi/180
        cos = math.cos(convert_angle)
        sin = math.sin(convert_angle)
        invRotMatrix = np.array([[cos, sin], [-sin, cos]])  #Inverse Rotation matrix an array of floats
        return invRotMatrix

    def backwardRotation(self, p : RealPoint) -> RealPoint:
        rp = np.array([p.x-self.center.x,p.y-self.center.y])
        #Call getInverseRotationMatrix function to get the inverser rotation matrix
        rotMatrix = self.getInverseRotationMatrix()
        #Apply multiplication matrix between the point pr and the rotation matrix rotMatrix
        rotP = rotMatrix.dot(rp)
        return RealPoint(rotP[0]+self.center.x, rotP[1]+self.center.y)

    def digitizedBackwardRotation(self, p : RealPoint) -> ImagePoint:
        #Apply backardRotation function on point p
        rp = self.backwardRotation(p)
        #Call digitizeRealPoint function for rp to obtain a digitized point
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

#Create a black image of size [width, height]
def createBlackImage(width: int, height: int):
    image = np.zeros((height,width,1), np.uint8)
    return image

#Backward rotation of a given image
def backwardRotationImage(image_in, theta):
    #Get dimensions of image
    height, width = image_in.shape[:2]
    #Create a black image to store the transformed result
    image_out = createBlackImage(width,height)
    #Create an objet of rotation class for the rotation theta with center at RealPoint(width/2,height/2)
    rot = rotation(theta, RealPoint(width/2,height/2))
    #Realized the digitized backward rotation
    for i in range(width):#Col - x
        for j in range(height):#Row - y
            #Get the point in image
            p = RealPoint(i, j)
            #Call digitizedBackwardRotation to transform the point
            rp = rot.digitizedBackwardRotation(p)
            #Get the pixel value for the point (i,j) in the image
            v = getPixelValue(image_in, rp.row, rp.col)
            if(v!=-1): #If the pixel is in the image, then set the value to the point (i,j)
                setPixelValue(image_out, j, i, v)
    #Return the transformed result
    return image_out

#Compute the connected components for 4-connectivity
def connectedComponent(image_in):
    #Call connectedComponents function in OpenCV to label the connected component
    nb_labels, labels = cv.connectedComponents(image_in, connectivity=4)
    #Map component labels to hue value color
    label_hue = np.uint8(1000*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv.merge([label_hue, blank_ch, blank_ch])
    #Convert to color image for display
    labeled_img = cv.cvtColor(labeled_img, cv.COLOR_HSV2BGR)
    #Set background label to black
    labeled_img[label_hue==0] = 0
    return labeled_img

###################################
########### Main program ##########
###################################

#Read an image given the filename
#TODO: Change filename here
filename = "../Samples/retina_2.png"
img = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)

#Call backwardRotationImage on the input image img
angle = 45
backward_rot_image = backwardRotationImage(img, angle)
#Display the result
cv.imshow(title_window1, backward_rot_image)
#Save the result
cv.imwrite("../Results/backward_rotation_image.png", backward_rot_image)

#Call the connected component labelling on the transformed image
connected_component_image = connectedComponent(backward_rot_image)
#Display the result
cv.imshow(title_window2, connected_component_image)
#Save the result
cv.imwrite("../Results/connected_component_image.png", connected_component_image)

#Wait for any key then close all the windows
key = cv.waitKey()
cv.destroyAllWindows()
