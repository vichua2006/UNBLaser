import PIL.Image as Image
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm
import os

# 46 pixle = 1mm
# zoom: 125%

IMGDIR = r".\images\laser_beams\patch_3\\"
GRAPHDIR = r".\intensity_profile\patch_3\\"

def main():
    file_names = os.listdir(IMGDIR)

def graphSurface(src: str, dest: str):

    # Read image. 
    img = Image.open(src)

    # Convert to numpy array
    img_as_np = np.array(img)
    Y_len, X_len = img_as_np.shape

    x = np.arange(X_len)
    y = np.arange(Y_len)

    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    surf = ax.plot_surface(X, Y, img_as_np, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    ax.set_xlabel("Horizontal Position (pixels)")
    ax.set_ylabel("Vertical Position (pixels)")
    ax.set_zlabel("Brightness")
    plt.title("")

    plt.show()
    plt.savefig(dest)

