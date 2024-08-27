import numpy as np
import lmfit as lm
import matplotlib.pyplot as plt
import pandas as pd

def mySine(x, amp, freq, phi, C):
    # C: constant offset
    return amp * np.sin(2*np.pi*freq*x - phi) + C


ModelFile = 'Sine_Model.sav'

Model1 = lm.Model(mySine)
Pars1  = Model1.make_params(amp=1., freq=0.25, phi=1., C=400)
Pars1['amp'].max = 1000.
Pars1['amp'].min = 0.
Pars1['freq'].max = np.inf
Pars1['freq'].min = 0.
Pars1['phi'].max = 10*np.pi
Pars1['phi'].min = 0.

df = pd.read_csv(r"..\HalfWavePlate\raw_data\aug_27.csv").to_numpy()
df = df[:-2]


x = df[ : , 1]
y = df[ : , 2]


result1 = Model1.fit(y, Pars1, x=x)
print(result1.fit_report())

plt.plot(x, y, 'bo')
plt.plot(x, result1.best_fit, 'r-')

plt.show()