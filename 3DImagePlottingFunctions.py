import PIL.Image as Image
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm
import os

# 46 pixle = 1mm
# zoom: 125%

IMGDIR = r".\images\laser_beams\patch_3\\"
GRAPHDIR = r".\intensity_profile\patch_3\\"

def loadFiles(dir: str) -> str:
    file_names = os.listdir(dir)
    return file_names

def loadImageAsArray(dir: str):
    # Read image. 
    img = Image.open(dir)
    # Convert to numpy array
    arr = np.array(img)

    return arr


def graphSurface(src: str, dest: str, title: str):

    arr = loadImageAsArray(src)
    Y_len, X_len = arr.shape

    x = np.arange(X_len)
    y = np.arange(Y_len)

    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    surf = ax.plot_surface(X, Y, arr, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    ax.set_xlabel("Horizontal Position (pixels)")
    ax.set_ylabel("Vertical Position (pixels)")
    ax.set_zlabel("Brightness")
    plt.title(title)

    # plt.show()
    plt.savefig(dest, format="pdf")
    plt.close()

def main():
    file_names = loadFiles(IMGDIR)
    for full_name in file_names:
        title = full_name.split(".")[0]
        src = IMGDIR + full_name
        dest = rf"{GRAPHDIR}\{title}.pdf"
        graphSurface(src, dest, title)

if __name__ == "__main__":
    main()