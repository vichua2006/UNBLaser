import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import lmfit as lm

def Gaussian(x, amp, cen, wid, off):
	"""Simple model of 1D Gaussian function."""
	# adjusted width to reflect w = I/e^2
	return amp * np.exp(-2*((x-cen)/wid)**2) + off

def mySine(x, amp, freq, phi, C):
    # C: constant offset
    return amp * np.sin(2*np.pi*freq*x - phi) + C

def lmfit(x: np.ndarray, y: np.ndarray, title: str, dest_dir: str, p: dict[str, float], func):
	"""Plot a general fit curve of a set of data
	params: [name of parameter: inital guess]	
	"""

	ShowInitialGuess = True

	model  = lm.Model(func)

	# creates a parameters objects
	params = lm.Parameters()

	# add parameters
	for parameter in p:
		params.add(lm.Parameter(name=parameter,value=p[parameter], vary=True, min=-np.inf, max=np.inf))

	# fit the curve to those parameters 
	result = model.fit(y, params, x=x)

	# give a report on the parameters
	print(result.fit_report())
	# write the report into a text file
	with open(f"{dest_dir}\\{title}.txt", "w") as f:
		f.write(result.fit_report())


	fig = plt.figure(figsize=(7,5), constrained_layout=True)
	wratios, hratios = ([1], [1, 3])
	gs  = fig.add_gridspec(nrows=2, ncols=1, width_ratios=wratios, height_ratios=hratios)
	ax1 = fig.add_subplot(gs[1,0])
	ax0 = fig.add_subplot(gs[0,0], sharex=ax1)
	axs = [ax0, ax1]
	plt.setp(ax0.get_xticklabels(), visible=False)

	axs[0].set_ylabel(r'$y - f(x)$')
	axs[1].set_xlabel(r'Position (mm)')
	axs[1].set_ylabel(r'Brightness')

	axs[0].plot(x, y-result.best_fit, color='black', marker='.', linestyle='', label='Residuals')
	axs[1].plot(x, y, color='black', marker='.', linestyle='', label='Data')
	axs[1].plot(x, result.best_fit, color='crimson', marker='', linestyle='-', label='Best fit')

	if ShowInitialGuess:
		axs[1].plot(x, result.init_fit, color='royalblue', marker='', linestyle='-', label='Initial guess')

	for ax in axs:
		ax.legend(loc='best')
		ax.grid()

	plt.title(title)
	plt.savefig(f"{dest_dir}\\{title}.pdf", format="pdf")
	plt.close()


def plotGaussian(x: np.ndarray, y: np.ndarray, title: str, dest_dir: str):

	init_amp = float(y.max())
	init_cen = np.ndarray.tolist(x)[np.argmax(y)]
	init_wid = 1
	init_off = 0


	# Parametered obtained from abritary initial parameters
	# init_amp = 0.325
	# init_cen = 8.367
	# init_wid = 0.435
	# init_off = 0.002
		
	ShowInitialGuess = True

	model  = lm.Model(Gaussian)
	# params = model.make_params()

	params = lm.Parameters()

	# Parameter definitions, initial guess
	params.add(lm.Parameter(name='amp', value=init_amp, vary=True, min=0., max=np.inf))
	params.add(lm.Parameter(name='cen', value=init_cen, vary=True, min=-np.inf, max=np.inf))
	params.add(lm.Parameter(name='off', value=init_off, vary=True, min=-np.inf, max=np.inf))
	params.add(lm.Parameter(name='wid', value=init_wid, vary=True, min=0., max=np.inf))

	# creates a parameters objects

	# fit the curve to those parameters 
	result = model.fit(y, params, x=x)

	# give a report on the parameters
	print(result.fit_report())
	# write the report into a text file
	with open(f"{dest_dir}\\{title}.txt", "w") as f:
		f.write(result.fit_report())


	fig = plt.figure(figsize=(7,5), constrained_layout=True)
	wratios, hratios = ([1], [1, 3])
	gs  = fig.add_gridspec(nrows=2, ncols=1, width_ratios=wratios, height_ratios=hratios)
	ax1 = fig.add_subplot(gs[1,0])
	ax0 = fig.add_subplot(gs[0,0], sharex=ax1)
	axs = [ax0, ax1]
	plt.setp(ax0.get_xticklabels(), visible=False)

	axs[0].set_ylabel(r'$y - f(x)$')
	axs[1].set_xlabel(r'Position (mm)')
	axs[1].set_ylabel(r'Brightness')

	axs[0].plot(x, y-result.best_fit, color='black', marker='.', linestyle='', label='Residuals')
	axs[1].plot(x, y, color='black', marker='.', linestyle='', label='Data')
	axs[1].plot(x, result.best_fit, color='crimson', marker='', linestyle='-', label='Best fit')

	if ShowInitialGuess:
		axs[1].plot(x, result.init_fit, color='royalblue', marker='', linestyle='-', label='Initial guess')

	for ax in axs:
		ax.legend(loc='best')
		ax.grid()

	plt.title(title)
	plt.savefig(f"{dest_dir}\\{title}.pdf", format="pdf")
	plt.close()

def main():
	df = pd.read_csv(r".\raw_data\(updatedAugust21)powerdata-August21(Victor).csv").to_numpy()


	x = df[ : , 0]
	y = df[ : , 3]

	p = {
		"amp" : float(y.max()),
		"cen" : np.ndarray.tolist(x)[np.argmax(y)],
		"wid" : 1.,
		"off" : 0.
	}

	lmfit(x, y, "title", ".\\", p, Gaussian)
	# plotGaussian(x, y, "title", ".\\")
	print(type(x))

if __name__ == "__main__":
	main()
