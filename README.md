# UNBLaser

A repo containing matplotlib scripts used to analyze the intensity profiles of various lasers

# Laser Intensity

Defined as the power per area of the laser (units of $\frac{W}{m^2}$) of a laser beam. Follows a [[Gaussian Distribution]], with the following equation\*:

$$
I(x) = I_0 \cdot e^{-2(\frac{x}{W_0})^2}
$$

where $x$ is the position along the diameter of the beam, $I_0$ is the intensity of the center (amplitude), and $W_0$ is the beam waist, defined as the position $x_w$ where $I(x_w) = I_0/e^2$

_(this whole thing is somewhat handwavy, because a 2D graph cannot fully represent the distribution since it's a 3D phenomenon_, see more in pdf)

# Graphing

Graphed with [matplotlib](https://matplotlib.org/)
