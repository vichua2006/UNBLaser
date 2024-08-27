from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from LMFIT import plotGaussian
from ConvertPixelsTomm import convertpixtomm

IMGSRC = r".\images\laser_beams\patch_3"
DEST = r".\intensity_profile\patch_3_2D\fitted"

def load_image(file_name: str):
    image = Image.open(file_name)
    image_array = np.array(image)
    return image_array

def position_arrays(image_array: np.ndarray):
    # returns the position array (x and y axes) of the image array
    height, width = image_array.shape
    x = np.arange(width)
    y = np.arange(height)
    xv, yv = np.meshgrid(x, y)
    x_pos = xv.flatten()
    y_pos = yv.flatten()
    realx = np.unique(x_pos)
    realy = np.unique(y_pos)
    brightness = image_array.flatten()
    return([realx, realy, brightness])

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

def sum_columns_rows(image_array):
  # Sum every column over every row
  column_sums = np.sum(image_array, axis=0)
  # Sum every row over every column
  row_sums = np.sum(image_array, axis=1)
  return column_sums, row_sums

def main():
    file_names = os.listdir(IMGSRC)

    for full_name in file_names:
        name = full_name.split(".")[0]
        src = f"{IMGSRC}\\{full_name}"  
        arr = load_image(src)

        new_dir = f"{DEST}\\{name}"
        os.makedirs(new_dir)

        x, y, _ = position_arrays(arr)
        x, y = convertpixtomm(x, y)
        cs, rs = sum_columns_rows(arr)
        plotGaussian(x, cs, name + "x", new_dir)
        plotGaussian(y, rs, name + "y", new_dir)
    

if __name__ == "__main__":
    main()