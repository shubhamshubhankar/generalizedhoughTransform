import numpy as np
from scipy.ndimage import convolve
from build_reference_table import *
from skimage import io
import matplotlib.pyplot as plt
from skimage.io import imread, imshow

def drawBoxes(acc, refim, im, val, ridx, cidx):
    # Code for drawing bounding-box in accumulator array...

        acc[ridx - 5:ridx + 5, cidx - 5] = val
        acc[ridx - 5:ridx + 5, cidx + 5] = val

        acc[ridx - 5, cidx - 5:cidx + 5] = val
        acc[ridx + 5, cidx - 5:cidx + 5] = val

        plt.figure(1)
        imshow(acc)
        plt.show()

        # Code for drawing bounding-box in original image at the found location...

        # Find the half-width and height of template
        hheight = np.floor(refim.shape[0] / 2) + 1
        hwidth = np.floor(refim.shape[1] / 2) + 1

        # Find coordinates of the box
        rstart = int(max(ridx - hheight, 1))
        rend = int(min(ridx + hheight, im.shape[0] - 1))
        cstart = int(max(cidx - hwidth, 1))
        cend = int(min(cidx + hwidth, im.shape[1] - 1))

        # Draw the box
        im[rstart:rend, cstart] = 255
        im[rstart:rend, cend] = 255

        im[rstart, cstart:cend] = 255
        im[rend, cstart:cend] = 255

        # Show the image
        plt.figure(2), imshow(refim)
        plt.figure(3), imshow(im)
        plt.show()
