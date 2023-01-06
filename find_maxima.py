import numpy as np

def findMaxima(accumulatorArray):
    """
    :param acc: accumulator array
    :return:
        maxval: maximum value found
        ridx: row index of the maxval
        cidx: column index of the maxval
    """
    #print("argmax ")
    #print(acc.argmax())
    ridx, cidx = np.unravel_index(accumulatorArray.argmax(), accumulatorArray.shape)
    return [accumulatorArray[ridx, cidx], ridx, cidx]
