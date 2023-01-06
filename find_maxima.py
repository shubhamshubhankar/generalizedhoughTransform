import numpy as np

def findMaxima(acc):
    """
    :param acc: accumulator array
    :return:
        maxval: maximum value found
        ridx: row index of the maxval
        cidx: column index of the maxval
    """
    #print("argmax ")
    #print(acc.argmax())
    ridx, cidx = np.unravel_index(acc.argmax(), acc.shape)
    return [acc[ridx, cidx], ridx, cidx]
