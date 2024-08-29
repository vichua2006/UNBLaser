# UNBLaser

A repo containing matplotlib scripts used to analyze the intensity profiles of various lasers

# Laser Intensity

Defined as the power per area of the laser (units of $\frac{W}{m^2}$) of a laser beam. Follows a [Gaussian Distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution), with the following equation\*:

$$
I(x) = I_0 \cdot e^{-2(\frac{x}{W_0})^2}
$$

where $x$ is the position along the diameter of the beam, $I_0$ is the intensity of the center (amplitude), and $W_0$ is the beam waist, defined as the position $x_w$ where $I(x_w) = I_0/e^2$

_(this whole thing is somewhat handwavy, because a 2D graph cannot fully represent the distribution since it's a 3D phenomenon_, see more in pdf)

# Graphing

Graphed with [matplotlib](https://matplotlib.org/)
Example graphs are camera trial data, with exposure at 600 ms

### Image

![exp600](https://github.com/vichua2006/UNBLaser/blob/main/README_images/Exp600.png)

### 2D Profile

(summed columns of image)
![exp600-2D](https://github.com/vichua2006/UNBLaser/blob/main/README_images/2D%20Intensity%20Profile.png)

### 3D Profile

![exp600-3D](https://github.com/vichua2006/UNBLaser/blob/main/README_images/3D%20Intensity%20Profile.png)
