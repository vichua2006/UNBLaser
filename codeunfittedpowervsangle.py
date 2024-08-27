import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('default') 

df=pd.read_csv('halfwaveplate.csv')
df=df[:-2]


fig, axs = plt.subplots()

# Populate the axis with a few plots:
x = df['Measured Angle (radians)']
yparallel= df['Power [Parallel To Original To Beam] (nW)']
yperp= df['Power [Perpendicular To Original To Beam] (nW)']
axs.plot(x,yparallel, 'mo', label='parallel detector') 
axs.plot(x,yperp, 'bo', label='perp detector')
axs.title.set_text('unfitted Power(nW) vs Position radians')
# To set the x & y labels on an axis, we must use the 'set_xlabel' and 'set_ylabel' methods:
axs.set_xlabel('x (rad)')
axs.set_ylabel('power(nW)')
# Note that plt.xlabel() and plt.ylabel() place labels on the current Figure object, not on a given Axis. 
# In this example, because the figure contains only one axis, plt.xlabel() and plt.ylabel() will also work here.

# To activate the legend and grid lines on this axis:
axs.legend()
axs.grid()

# Show the entire figure:
plt.show()