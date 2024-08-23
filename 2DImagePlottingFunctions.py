from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

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

#Example
'''
scatter_plot(position_arrays(load_image('exp200.tiff'))[0], position_arrays(load_image('exp200.tiff'))[1], position_arrays(load_image('exp200.tiff'))[2])
'''
