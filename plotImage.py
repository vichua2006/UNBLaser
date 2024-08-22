import PIL.Image as Image
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm

# 46 pixle = 1mm
# zoom: 125%

PATH = r".\images\cutout\exposure5500.jpg"
  
# Read image. 
img = Image.open(PATH).convert("L")

# Convert to numpy array
img_as_np = np.asarray(img)
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

plt.show()

