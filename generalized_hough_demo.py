#!/usr/bin/env python

from skimage.io import imread, imshow
import matplotlib.pyplot as plt
from build_reference_table import *
from match_table import *
from find_maxima import *
import cv2
import numpy as np

images = ['Input1Ref.png', 'Input2Ref.png', 'Input3Ref.png', 'Input4Ref.png']
'''
Looping these two images to create separate identification.
'''
for img in images:
    
    #This is the smaller image which we have to find in the bigger image.
    refim = cv2.imread(img)

    #Converting the RGB image to a grayscale image.
    refim = cv2.cvtColor(refim, cv2.COLOR_RGB2GRAY)
   
    #This is the larger image where we have to search the smaller image.
    im = imread('Input1.png')

    #Building the reference table from refim.
    table = buildRefTable(refim)

    # Increase the values in the accumulator table using reference table.
    acc = matchTable(im, table)

    # Find the maximum from the accumulator table
    # val: maximum value found
    # ridx: row index of the maxval
    # cidx: column index of the maxval
    val, ridx, cidx = findMaxima(acc)

    print("val ")
    print(val)

    print("ridx: ", ridx, ", cidx: ", cidx)
    
    # Code for drawing bounding-box in accumulator array...

    acc[ridx - 5:ridx + 5, cidx - 5] = val
    acc[ridx - 5:ridx + 5, cidx + 5] = val

    acc[ridx - 5, cidx - 5:cidx + 5] = val
    acc[ridx + 5, cidx - 5:cidx + 5] = val

    plt.figure(1)
    imshow(acc)
    plt.show()

    # code for drawing bounding-box in original image at the found location...

    # find the half-width and height of template
    hheight = np.floor(refim.shape[0] / 2) + 1
    hwidth = np.floor(refim.shape[1] / 2) + 1

    # find coordinates of the box
    rstart = int(max(ridx - hheight, 1))
    rend = int(min(ridx + hheight, im.shape[0] - 1))
    cstart = int(max(cidx - hwidth, 1))
    cend = int(min(cidx + hwidth, im.shape[1] - 1))

    # draw the box
    im[rstart:rend, cstart] = 255
    im[rstart:rend, cend] = 255

    im[rstart, cstart:cend] = 255
    im[rend, cstart:cend] = 255

    # show the image
    plt.figure(2), imshow(refim)
    plt.figure(3), imshow(im)
    plt.show()
