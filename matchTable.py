
import numpy as np
from scipy.ndimage import convolve
from buildReferenceTable import *
from skimage import io
import matplotlib.pyplot as plt


def matchTable(mainImage, table):
    
    # matches the reference table with the given input
    # image for testing generalized Hough Transform
    # m, n = im.shape
    rows= mainImage.shape[0]
    cols = mainImage.shape[1]

    # accumulator array requires some extra space
    accumulatorArray = np.zeros((rows+100, cols+100))  
    
    # Function to find the gradient given coordinate x and y.
    def findGradient(x, y):
      if x != 0:
        return int(np.rad2deg(np.arctan(int(y/x))))
      else:
        return 0
    #print(acc.shape)
    # The row runs from 1 to 306.
    # The column runs from 1 to 306.

    for x in range(1, rows):
        for y in range(1, cols):
            
            # Because it's a binary image, all the points which
            # are not black are boundary points.
            #print("x : ",x , " y: ", y, "\n")
            #print(im[x])
            if mainImage[x, y] != 0:  # boundary point
                
                # Finds the gradient from the current point and
                # stores it into theta.
                theta = findGradient(x, y)
                
                # Finds the list for that theta from the reference image
                # and stores it into vectors.
                vectors = table[theta]
                
                # Casting of the votes has been done here.
                for vector in vectors:
                    accumulatorArray[vector[0]+x, vector[1]+y] += 1
    return accumulatorArray
