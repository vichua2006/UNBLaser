import numpy as np
import pandas as pd

def FindG(x, y):
    amp = max(y) - min(y)
    cen = x[np.argmax(y)]
    # wid = waist(x, y)
    off = -1 * min(y)

    return (amp, cen, off)

def search(arr: np.ndarray, value):
    n = arr.size
    idx = 0



# Read in the csv with pandas as a np array
df = pd.read_csv(r".\raw_data\(updatedAugust21)powerdata-August21(Victor).csv").to_numpy()

x = df[ : , 0]
y = df[ : , 3]

wid_y = y.max()/7.38905


