import math
import numpy as np

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
    theta: None  # float, rotation angle in degree
    center : None # center of rotation
    rotMatrix : None #Rotation matrix from given angle (in degree)

    def __init__(self, angle_):
        self.theta = angle_
        self.center = RealPoint(0,0)
        convert_angle = self.theta * math.pi / 180 #Convert angle from degrees to rads
        cos = math.cos(convert_angle)
        sin = math.sin(convert_angle)
        self.rotMatrix = np.array([[cos, -sin], [sin, cos]])  #Rotation matrix an array of floats

    def __init__(self, angle_, center_):
        self.theta = angle_
        self.center = center_
        convert_angle = self.theta * math.pi / 180
        cos = math.cos(convert_angle)
        sin = math.sin(convert_angle)
        self.rotMatrix = np.array([[cos, -sin], [sin, cos]])  #Rotation matrix an array of floats

    def getRotationMatrix(self):
        return self.rotMatrix

    def getInverseRotationMatrix(self):
        #TODO: initize the invers rotation matrix with -angle
        convert_angle = self.theta * math.pi / 180
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
        ip = rp.digitizeRealPoint()
        return ip

###################################
########### Main program ##########
###################################

#TODO: Create a real point of coordinate (5.2, 3.5)
rp = RealPoint(5.2, 3.5)
#Display the point
rp.printRealPoint()

#TODO: Digitize the created point rp
irp = rp.digitizeRealPoint()
#Display the digitized point
irp.printImagePoint()

#TODO: Create a discret point of coordinate (4, 5)
ip = ImagePoint(4, 5)
#Display the point
ip.printImagePoint()

#TODO: Create an objet of rotation class for a rotation of 45 degrees with center at RealPoint(0,0)
rot_test = rotation(45, RealPoint(0,0))

#TODO: Forward rotation the real point rp with the previous objet rot_test
rip = rot_test.forwardRotation(rp) #result is a RealPoint
#Display the point
rip.printRealPoint()

#TODO: Digitized forward rotation the discret point rp
drip = rot_test.digitizedForwardRotation(rp) #result is a ImagePoint
#Display the point
drip.printImagePoint()

#TODO: Digitized backward rotation the discret point rp
drip2 = rot_test.digitizedBackwardRotation(rp) #result is a ImagePoint
#Display the point
drip2.printImagePoint()
