import cv2 as cv
import numpy as np

title_window = "Input binary image"

#Function to read the value of a pixel in image
def getPixelValue(img, row : int, col : int) -> int:
    height,width = img.shape[:2] #Get the dimension of the image
    if(row<height and row>=0 and col<width and col>=0):
        return img[row,col]
    return -1

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
            #TODO: Get the four pixels that form a square of 2x2 (Indication: use getPixelValue for the four pixel (i,j), (i+1, j), (j+1,i), (i+1, j+1))
            a = getPixelValue(image_in, i, j)
            b = getPixelValue(image_in, i+1, j)
            c = getPixelValue(image_in, i, j+1)
            d = getPixelValue(image_in, i+1, j+1)
            #TODO: Call isFobidenWellComposedConfigutation to detect whether the four pixels form a non well-composed configuration
            if isFobidenWellComposedConfigutation(a, b, c, d)==True:
                return False #Image is not well-composed
    return True #No forbidden configuration detected, image is well-composed

###################################
########### Main program ##########
###################################

#Read an image given the filename
#TODO: Change filename here
filename = "../Samples/circles_2.png"
img = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
#Convert image to a binary image with threshold=125 for example
th_val, img_binary = cv.threshold(img,125,255,cv.THRESH_BINARY)
#Display the input binary image
cv.imshow(title_window,img_binary)

#TODO: call verifyWellComposedImage to verify the well-composedness of img_binary
is_well_composed = verifyWellComposedImage(img_binary)
#Display the result
if(is_well_composed):
    print("Input image is well-composed")
else:
    print("Input image is not well-composed")

###################################
## Optional: Connected component ##
###################################

#Compute the connected components for 4-connectivity
nb_labels, labels = cv.connectedComponents(img_binary, connectivity=4)

#Map component labels to hue value color
label_hue = np.uint8(1000*labels/np.max(labels))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv.merge([label_hue, blank_ch, blank_ch])

#Convert to color image for display
labeled_img = cv.cvtColor(labeled_img, cv.COLOR_HSV2BGR)

#Set background label to black
labeled_img[label_hue==0] = 0

#Display the labelled image
cv.imshow("Labelled image",labeled_img)
#Save the labelled image
cv.imwrite("../Results/labelled_image.png",labeled_img)

#Wait for any key then close all the windows
key = cv.waitKey()
cv.destroyAllWindows()
