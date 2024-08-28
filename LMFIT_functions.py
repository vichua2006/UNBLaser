import numpy as np

def Gaussian(x, amp, cen, wid, off):
	"""Simple model of 1D Gaussian function."""
	# adjusted width to reflect w = I/e^2
	return amp * np.exp(-2*((x-cen)/wid)**2) + off

def Sinusoidal(x, amp, freq, phi, off):
    # C: constant offset
    return amp * np.sin(2*np.pi*freq*(x - phi)) + off

def fixedSinusoidal(x, amp1, amp2, phi, off):
	return np.square((amp1 * np.cos(2 * np.pi * (x - phi)) + amp2 * np.cos(4 * np.pi * (x - phi)))) + off

def ComplexExp(x, amp, freq, phi, off):
	return amp * np.exp(2j * np.pi * freq * (x - phi)) + off

def complexSum(x, amp1, amp2, freq1, freq2, phi1, phi2, off):
	return ComplexExp(x, amp1, freq1, phi1, 0) + ComplexExp(x, amp2, freq2, phi2, 0) + off

def realSum(x, amp1, amp2, freq1, freq2, phi1, phi2, off):
	return np.real(complexSum(x, amp1, amp2, freq1, freq2, phi1, phi2, off))

def sineSum(x, amp1, amp2, freq1, freq2, phi1, phi2, off):
	return Sinusoidal(x, amp1, freq1, phi1, 0) + Sinusoidal(x, amp2, freq2, phi2, 0) + off
