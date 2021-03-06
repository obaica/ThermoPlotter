#!/usr/bin/env python3

import matplotlib.pyplot as plt
import tp

phile = 'data/zno/band.yaml'
kappafile = 'data/zno/kappa-m404021.hdf5'
poscar = 'data/zno/POSCAR'
temperature = 300

colour = 'viridis' #tp.plot.colour.linear('#ff0000', '#000000')

# Axes

fig, ax = tp.axes.one.plain(['tp', 'dark_background'])

# Load

data = tp.data.load.phono3py(kappafile, quantities='wideband')
pdata = tp.data.load.phonopy_dispersion(phile)

# Add

tp.plot.phonons.add_wideband(ax, data, pdata, temperature=temperature,
                             colour=colour, poscar=poscar)

# Save

plt.savefig('wideband.pdf')
plt.savefig('wideband.png')
