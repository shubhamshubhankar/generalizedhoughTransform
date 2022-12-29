#!/usr/bin/env python

__author__ = "Adeel Ahmad"
__email__ = "adeelahmad14@hotmail.com"
__status__ = "Production"

import numpy as np
from scipy.ndimage import convolve
from skimage import io
import matplotlib.pyplot as plt


def buildRefTable(img):
    """
    builds the reference table for the given input template image
    :param im: input binary image
    :return:
        table = a reconstructed reference table...
    """
    table = [[0 for x in range(1)] for y in range(90)]  # creating a empty list

    print(img.shape)
    #print(len(table[0]))
    #print(table)
    
    # r will be calculated corresponding to this point
    img_center = [int(img.shape[0]/2), int(img.shape[1]/2)]
    print(img_center)

    print(img)
   
    #  This function takes input one point with x and y coordinates
    #  and then calculate the distance from the center and also 
    #  the angle from the center.
    def findAngleDistance(x1, y1):
        x2, y2 = img_center[0], img_center[1]
        r = [(x2-x1), (y2-y1)]
        if (x2-x1 != 0):
            return [int(np.rad2deg(np.arctan(int((y2-y1)/(x2-x1))))), r]
        else:
            return [0, 0]

    filter_size = 3


    # The loop with go over the image and will run from
    # 1 to 69 in the row direction and from 1 to 71 in the
    # column direction.
    for x in range(img.shape[0]-(filter_size-1)):
        for y in range(img.shape[1]-(filter_size-1)):
        # As our image is a binary image, we will only
        # calculate the distance from the points which are
        # non-zero.
            if (img[x, y] != 0):
            # The distance from the center is called r and the
            # angle is called theta.
                theta, r = findAngleDistance(x, y)
                # If the distance from center is non-zero, we
                # will store it into our table.
                if (r != 0):
                    '''
                    print("theta ", theta)
                    print("\n")
                    print("r ", r)
                    print("\n")
                    '''
                    table[np.absolute(theta)].append(r)

    #print("Before popping \n")
    #print(table)
    
    # Remove all the zero values from the table.
    for i in range(len(table)):
        table[i].pop(0)

    #print("After popping \n")
    for i in range(len(table)):
        print(i)
        print(" ")
        print(table[i])

    return table
        
