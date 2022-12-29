import cv2
import numpy as np
from PIL import Image

img=cv2.imread("image.jpg")
#imread method loads an image from the specified file

grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cvtColor() method is used to convert an image from one color space to another
#why it is convert to greyscale
'''Importance of grayscaling
Reduces model complexity: Consider training neural articles on RGB images of 10x10x3 pixels. 
The input layer will have 300 input nodes.
 On the other hand, the same neural network will need only 100 input nodes for grayscale images.'''

grey=cv2.medianBlur(grey,3 )
#Blurring the image for smoother texture
#It has two parameters ,one is image and the second is intensity of blur

edges=cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,13,6)
#It is used to specify that what are the edges of the face
'''Specifying a threshold that if the color intensity of a specific color is this,
then make it as the egde'''
#adaptiveThreshold(source, maxVal, adaptiveMethod, thresholdType, blocksize, constant)
'''The first parameter is grey image and second image is intensity
third is used to decide how threshold value is calculated ,fourth parameter
is used to find the type of thresholding to be applied,fifth is size of pixel(thickness of image)
 and sixth is constant value that is subtracted from mean(detailed ness of image)
'''

color=cv2.bilateralFilter(img,9,250,250)
#bilateral filter which is basically smoothing only

cartoon=cv2.bitwise_and(color,color,mask=edges)
#used to extract essential parts of image
#the first and second are smoothing filter and the third is
# the mask the edges.

cv2.imshow("show",cartoon)

pil_image=Image.fromarray(cartoon)
pil_image.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

