import numpy as np

def cosineSquared(x, amp, off, phase) -> np.ndarray:
	return (amp * (np.cos(2* (x - phase))) + off) ** 2

def exponentialX(X: float):
    return np.exp(-1j * X)

def outside(eta: float):
    return np.exp(-1j * eta / 2)

# refering to jones matrix
def B(eta: float, phi: float, theta: float):
    return outside(eta) * ((1 - exponentialX(eta)) * exponentialX(phi) * np.cos(theta) * np.sin(theta))  

def D(eta: float, theta: float):
    return outside(eta) * (np.sin(theta) ** 2 + exponentialX(eta) * np.cos(theta) ** 2)

def matrix(eta: float, phi: float, theta: float):
    B_value = B(eta, phi, theta) 
    D_value = D(eta, theta) 

    return B_value * np.conjugate(B_value) + D_value * np.conjugate(D_value)

def power(x: np.ndarray, amp: float, phase: float, off: float, eta: float, phi: float, theta: float):
    m = matrix(eta, phi, theta)
    s = cosineSquared(x, amp, off, phase)
    return m * s