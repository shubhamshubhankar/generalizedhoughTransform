
import numpy as np
from scipy.ndimage import convolve
from build_reference_table import *
from skimage import io
import matplotlib.pyplot as plt


def matchTable(im, table):
    """
    :param im: input binary image, for searching template
    :param table: table for template
    :return:
        accumulator with searched votes
    """
    # matches the reference table with the given input
    # image for testing generalized Hough Transform
    # m, n = im.shape
    m = im.shape[0]
    n = im.shape[1]
    acc = np.zeros((m+100, n+100))  # accumulator array requires some extra space
    
    #print(acc.shape)

    def findGradient(x, y):
        if x != 0:
            return int(np.rad2deg(np.arctan(int(y/x))))
        else:
            return 0

    # The row runs from 1 to 306.
    # The column runs from 1 to 306.

    for x in range(1, im.shape[0]):
        for y in range(1, im.shape[1]):
            
            # Because it's a binary image, all the points which
            # are not black are boundary points.
            #print("x : ",x , " y: ", y, "\n")
            #print(im[x])
            if im[x, y] != 0:  # boundary point
                
                # Finds the gradient from the current point and
                # stores it into theta.
                theta = findGradient(x, y)
                # Finds the list for that theta from the reference image
                # and stores it into vectors.
                vectors = table[theta]

                for vector in vectors:
                    acc[vector[0]+x, vector[1]+y] += 1
    return acc
