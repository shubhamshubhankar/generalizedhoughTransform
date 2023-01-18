import matplotlib.pyplot as plt
from buildReferenceTable import *
from matchTable import *
from drawBoxes import *
from findMaxima import *
import cv2
import numpy as np
from skimage.io import imread, imshow
import sys
import getopt

#images = ['Input1Ref.png', 'Input2Ref.png', 'Input3Ref.png', 'Input4Ref.png']


if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            print(
                "\n-----------------------------------------------------------------------------------------------------------------------\n"
                "This is a python implementation of the Generalized Hough Transform. \n"
                "Note: It only searches for the reference image of same size and orientation. \n\n"
                "Usage given below:\n"
                "python3 generalizedHoughDemo.py 'mainImageName' 'referenceImageName'\n\n"
                "All the arguements in this program are mandatory.\n"
                "Arguement List:\n"
                "mainImageName - Path of the image + name of the main(larger) image (String data type). \n"
                "referenceImageName - Path of the image + name of the reference(smaller) image (String data type).\n"
                "Example : \n"
                "python3 generalizedHoughDemo.py Input1.png Input1Ref.png\n"
                "\n----------------------------------------------------------------------------------------------------------------------\n")
            exit(0)
        else:
            mainImageName = sys.argv[1]
            referenceImageName = sys.argv[2]
    
        #This is the smaller image which we have to find in the bigger image.
        referenceImage = cv2.imread(referenceImageName)
        
        #im = cv2.imread('Input1.png')
        mainImage = cv2.imread(mainImageName)
        
        #Converting the RGB image to a grayscale image.
        referenceImage = cv2.cvtColor(referenceImage, cv2.COLOR_RGB2GRAY)
        mainImage = cv2.cvtColor(mainImage, cv2.COLOR_RGB2GRAY)
        
        #Building the reference table from refim.
        table = buildRefTable(referenceImage)

        # Increase the values in the accumulator table using reference table.
        accumulatorArray = matchTable(mainImage, table)

        # Find the maximum from the accumulator table
        # val: maximum value found
        # rowIndex: row index of the maxval
        # colIndex: column index of the maxval
        maximaValue, rowIndex, colIndex = findMaxima(accumulatorArray)

        '''
        # Printing the values with the rows and cols.
        print("val ")
        print(val)

        print("ridx: ", ridx, ", cidx: ", cidx)
        '''

        # Function to draw the boxes and plot the accumulator array.
        drawBoxes(accumulatorArray, referenceImage, mainImage, maximaValue, rowIndex, colIndex)
    
    except getopt.error as err:
        print(str(err))
            
