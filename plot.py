
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

def poly(x,a,b,c):
    return x*x*a+x*b+c

def line(x, a, b):
    return a * x + b 

class Data:
    def __init__(self, title, data):
        self.title = title
        self.data = np.array(data)

Current = Data("Current (mA)", [		64.8,	69.7,	74.7,	79.8,	84.8,	89.8,	94.8,	99.8])
Wavelength = Data("Wavelength (nm)", [		779.866,	779.869,	779.891,	779.897,	779.9,	779.921,	779.925,	779.929])
Power = Data("Power (mW)",[	3.601,	4.25,	4.88,	5.26,	5.84,	6.7,	6.78,	6.71] )
PDCurrent = Data("PD Current (mA)", [0.19,	0.226,	0.222,	0.307,	0.331,	0.309,	0.333,	0.375,])

allData = [Current, Wavelength, Power, PDCurrent]

for i in range(4):
    for j in range(i + 1, 4):
        for func in [line, line]:
            data1, data2 = allData[i], allData[j]

            plt.figure(figsize=(10,10), dpi=100)
            popt, pcov = scipy.optimize.curve_fit(func, data1.data, data2.data)
            try: plt.plot(data1.data,func(data1.data,popt[0],popt[1],popt[2]))
            except: plt.plot(data1.data,func(data1.data,popt[0],popt[1]))
            plt.plot(data1.data,data2.data,color="red")

            plt.xlabel(data1.title,fontsize=15,fontweight='bold')
            plt.ylabel(data2.title,fontsize=15, fontweight='bold')
            plt.legend()
            plt.grid()

            plt.savefig(rf".\plots\{data1.title}-{data2.title}.png")
            plt.close()
            plt.cla()

            print(f"{data1.title}-{data2.title}, {popt[0]}, {popt[1]}")
            

# print(popt[0],popt[1],popt[2])