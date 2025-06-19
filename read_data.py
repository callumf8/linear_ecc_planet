# ----------------------------------- #
# read_data.py
# Example script for reading in the linear theory
# torque data and AMF from Fairbairn & Dittmann (2025).
# ----------------------------------- #

import numpy as np
import matplotlib.pyplot as plt

# Set the data directory path
datadir = '.'

# Set the disc parameters and eccentricity
p = 0.5    # Surface density power law exponent
q = 0.0    # Temperature powerlaw exponent
e = 0.01   # Eccentricity

target_dir = datadir+'/p_{0}_q_{1}/e_{2}/'.format(p,q,e)

rgrid = np.loadtxt(target_dir+'rgrid.out')
dTdr = np.loadtxt(target_dir+'dTdr.out')
amf  = np.loadtxt(target_dir+'amf.out')

plt.plot(rgrid, dTdr, label=f'p={p}, q={q}, e={e}')
plt.plot(rgrid, amf, label=f'p={p}, q={q}, e={e} AMF')

plt.show()


