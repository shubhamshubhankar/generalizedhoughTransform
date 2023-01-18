import numpy as np
from scipy.ndimage import convolve
from buildReferenceTable import *
from skimage import io
import matplotlib.pyplot as plt
from skimage.io import imread, imshow

def drawBoxes(accumulatorArray, referenceImage, mainImage, maximaValue, rowIndex, colIndex):

        # Code for drawing bounding-box in accumulator array of 10*10 size 
        # where maxima values were found.
        accumulatorArray[rowIndex - 5:rowIndex + 5, colIndex - 5] = maximaValue
        accumulatorArray[rowIndex - 5:rowIndex + 5, colIndex + 5] = maximaValue

        accumulatorArray[rowIndex - 5, colIndex - 5:colIndex + 5] = maximaValue
        accumulatorArray[rowIndex + 5, colIndex - 5:colIndex + 5] = maximaValue

        plt.figure(1)
        imshow(accumulatorArray)
        plt.show()

        # Code for drawing bounding-box in original image at the found location...

        # Find the half-width and height of template
        halfHeight = np.floor(referenceImage.shape[0] / 2) + 1
        halfWidth = np.floor(referenceImage.shape[1] / 2) + 1

        # Find coordinates of the box
        rowStart = int(max(rowIndex - halfHeight, 1))
        rowEnd = int(min(rowIndex + halfHeight, mainImage.shape[0] - 1))
        colStart = int(max(colIndex - halfWidth, 1))
        colEnd = int(min(colIndex + halfWidth, mainImage.shape[1] - 1))

        # Draw the box
        mainImage[rowStart:rowEnd, colStart] = 255
        mainImage[rowStart:rowEnd, colEnd] = 255

        mainImage[rowStart, colStart:colEnd] = 255
        mainImage[rowEnd, colStart:colEnd] = 255

        # Show the image
        plt.figure(2), imshow(referenceImage)
        plt.figure(3), imshow(mainImage)
        plt.show()
