
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def sum_columns_rows(image_array):

    column_sums = np.sum(image_array, axis=1)
    row_sums = np.sum(image_array, axis=1)
    return column_sums, row_sums

def load_image(file_name):
    image = Image.open(file_name)
    image_array = np.array(image)
    return image_array

def position_arrays(image_array):
    height, width = image_array.shape
    x = np.arange(width)
    y = np.arange(height)
    xv, yv = np.meshgrid(x, y)
    x_pos = xv.flatten()
    y_pos = yv.flatten()
    brightness = image_array.flatten()
    return([x_pos, y_pos, brightness])

def scatter_plot(x_pos, y_pos, brightness):
    plt.figure()
    plt.scatter(x_pos, y_pos, c=brightness, cmap='gray', s=1)
    plt.colorbar()
    plt.figure()
    plt.scatter(x_pos, brightness)
    plt.xlabel("x-position")
    plt.ylabel("brightness")
    plt.figure()
    plt.scatter(y_pos, brightness)
    plt.xlabel("y-position")
    plt.ylabel("brightness")
    plt.show()
deltax = 0.007972665 #mm/pixel
deltay = 0.007575757 #mm/pixel

#returns list of x, y arrays
def convertpixtomm(xarray, deltax, yarray, deltay):
    xarraymm = xarray*deltax
    yarraymm = yarray*deltay
    return xarraymm, yarraymm

#scatter_plot
x,y,bright = position_arrays(load_image('exp1000.tiff'))[0], position_arrays(load_image('exp1000.tiff'))[1], position_arrays(load_image('exp1000.tiff'))[2]
realx, realy = convertpixtomm(np.unique(x), deltax,np.unique(y), deltay)
# realy = np.unique(y)
imarray = load_image('exp1000.tiff')
column_sums, row_sums = sum_columns_rows(imarray)
plt.figure()
plt.scatter(realx, column_sums)
plt.xlabel("position mm")
plt.ylabel("brightness")
plt.title("brightness vs. X pos")
plt.figure()
plt.scatter(realy, row_sums)
plt.xlabel("position mm")
plt.ylabel("brightness")
plt.title("brightness vs. Y pos")
plt.show()