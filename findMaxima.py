import numpy as np

def findMaxima(accumulatorArray):
    #print("argmax ")
    #print(acc.argmax())
    rowIdx, colIdx = np.unravel_index(accumulatorArray.argmax(), accumulatorArray.shape)
    return [accumulatorArray[rowIdx, colIdx], rowIdx, colIdx]
