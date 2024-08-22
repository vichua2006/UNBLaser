import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
plt.figure(figsize=(10,10), dpi=100)

def poly(x,a,b,c):
    return x*x*a+x*b+c

X=[		64.8,	69.7,	74.7,	79.8,	84.8,	89.8,	94.8,	99.8,
]
Y=[		779.866,	779.869,	779.891,	779.897,	779.9,	779.921,	779.925,	779.929,
]

Z=[	3.601,	4.25,	4.88,	5.26,	5.84,	6.7,	6.78,	6.71,	
]

X=np.array(X)
Y=np.array(Y)
Z=np.array(Z)

popt, pcov = scipy.optimize.curve_fit(poly, X, Y)
plt.plot(X,poly(X,popt[0],popt[1],popt[2]))
plt.plot(X,Y,color="red")

plt.xlabel("Current (mA)",fontsize=15,fontweight='bold')
plt.ylabel("$\\lambda$ (nm)",fontsize=15, fontweight='bold')
plt.legend()
plt.grid()

plt.show()

# print(popt[0],popt[1],popt[2])