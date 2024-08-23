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
