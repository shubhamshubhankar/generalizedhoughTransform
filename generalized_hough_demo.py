import matplotlib.pyplot as plt
from build_reference_table import *
from match_table import *
from drawBoxes import *
from find_maxima import *
import cv2
import numpy as np
from skimage.io import imread, imshow

images = ['Input1Ref.png', 'Input2Ref.png', 'Input3Ref.png', 'Input4Ref.png']


if __name__ == "__main__":
    #Looping these two images to create separate identification.
    for img in images:
        
        #This is the smaller image which we have to find in the bigger image.
        refim = cv2.imread(img)
        
        #This is the larger image where we have to search the smaller image.
        im = cv2.imread('Input1.png')
        
        #Converting the RGB image to a grayscale image.
        refim = cv2.cvtColor(refim, cv2.COLOR_RGB2GRAY)
        im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
        
        #Building the reference table from refim.
        table = buildRefTable(refim)

        # Increase the values in the accumulator table using reference table.
        acc = matchTable(im, table)

        # Find the maximum from the accumulator table
        # val: maximum value found
        # ridx: row index of the maxval
        # cidx: column index of the maxval
        val, ridx, cidx = findMaxima(acc)

        '''
        # Printing the values with the rows and cols.
        print("val ")
        print(val)

        print("ridx: ", ridx, ", cidx: ", cidx)
        '''

        # Function to draw the boxes and plot the accumulator array.
        drawBoxes(acc, refim, im, val, ridx, cidx)

        