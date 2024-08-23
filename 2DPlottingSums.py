# -*- coding: utf-8 -*-
#plottingsums

import numpy as np
import matplotlib.pyplot as plt

def sum_columns_rows(image_array):
  # Sum every column over every row
  column_sums = np.sum(image_array, axis=0)
  # Sum every row over every column
  row_sums = np.sum(image_array, axis=1)
  return column_sums, row_sums

realx = np.unique(x_pos)
realy = np.unique(y_pos)
column_sums, row_sums = sum_columns_rows(image_array)

plt.figure()
plt.scatter(realx, column_sums)
plt.figure()
plt.scatter(realy, row_sums)
plt.show()

# prompt: plot two subfigure scatterplots, with same y-axis (brightness), different x axis (x position or y posititon) x and y different sizes

import matplotlib.pyplot as plt
def subplots_scatter_diff_size(x_pos, y_pos, brightness):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # Adjust figsize for different sizes
    axs[0].scatter(x_pos, brightness)
    axs[0].set_xlabel("x-position")
    axs[0].set_ylabel("brightness")
    axs[1].scatter(y_pos, brightness)
    axs[1].set_xlabel("y-position")
    axs[1].set_ylabel("brightness")
    plt.show()

subplots_scatter_diff_size(realx, realy, brightness)
