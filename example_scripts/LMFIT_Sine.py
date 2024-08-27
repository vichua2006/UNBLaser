import numpy as np
import lmfit as lm
import matplotlib.pyplot as plt

def mySine(x, amp, freq, phi, C):
    # C: constant offset
    return amp * np.sin(2*np.pi*freq*x - phi) + C


ModelFile = 'Sine_Model.sav'

Model1 = lm.Model(mySine)
Pars1  = Model1.make_params(amp=1., freq=0.25, phi=1., C=0)
Pars1['amp'].max = 3.
Pars1['amp'].min = 0.
Pars1['freq'].max = np.inf
Pars1['freq'].min = 0.
Pars1['phi'].max = 2*np.pi
Pars1['phi'].min = 0.

x  = np.linspace(0., 3*np.pi, 101)
dy = np.random.normal(0, 0.1, x.size)
y1 = mySine(x, 1, 0.25, 1, 4) + dy

result1 = Model1.fit(y1, Pars1, x=x)
print(result1.fit_report())

plt.plot(x, y1, 'bo')
plt.plot(x, result1.best_fit, 'r-')

plt.show()