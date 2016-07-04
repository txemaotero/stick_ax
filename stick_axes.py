#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Descripción:

Se define una función para juntar los ejes de una figura
'''
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np


def stick_axes(fig, stick_x=True, stick_y=True):
    """
    Stick the axes of a figure 'fig'. The subplots distribution is respected.
    """
    # Se leen los ejes de la figura
    l_axes = fig.axes
    # El número de columnas y filas
    nrows, ncols, _, _ = l_axes[0].get_subplotspec().get_geometry()
    # Se inicia una lista de ceros con la forma del grid
    axes = [[0 for j in range(ncols)] for i in range(nrows)]
    # Se sitúa cada eje en su sitio de la grid
    for ax in l_axes:
        _, _, ind, _ = ax.get_subplotspec().get_geometry()
        row, col = ind//ncols, ind%ncols
        axes[row][col] = ax
    # Se quita el interespaciado
    if stick_x: plt.subplots_adjust(hspace=0.001)
    if stick_y: plt.subplots_adjust(wspace=0.001)
    # Se eliminan las etiquetas que queden en los intersticios
    # Primero en x
    if nrows > 1:
        if stick_y:
            for i in range(nrows-1):
                for j in range(ncols):
                    axes[i][j].set_xticklabels([])
            # Se eliminan las etiquetas que solapan
            nbins = len(axes[-1][-1].get_xticklabels())
            for j in range(nrows):
                for i in range(ncols-1):
                    axes[j][i].xaxis.set_major_locator(MaxNLocator(nbins=nbins, prune='upper'))
    # Ahora en y
    if ncols > 1:
        if stick_x:
            for j in range(ncols-1):
                for i in range(nrows):
                    axes[i][j+1].set_yticklabels([])
            # Se eliminan las etiquetas que solapan
            nbins = len(axes[-1][-1].get_xticklabels())
            for i in range(nrows-1):
                for j in range(ncols):
                    axes[i+1][j].yaxis.set_major_locator(MaxNLocator(nbins=nbins, prune='upper'))


fig = plt.figure()
ax1 = fig.add_subplot(421)
ax2 = fig.add_subplot(422)
ax3 = fig.add_subplot(423)
ax4 = fig.add_subplot(424)
ax5 = fig.add_subplot(425)
ax6 = fig.add_subplot(426)
ax7 = fig.add_subplot(427)
ax8 = fig.add_subplot(428)

x = np.linspace(-5,5,100)
y1 = np.cos(x)
y2 = x**2
y3 = x
y4 = x+3
y5 = x*0 -1

ax1.set_ylim([-6,6])
ax2.set_ylim([-6,6])
ax3.set_ylim([-6,6])
ax4.set_ylim([-6,6])
ax5.set_ylim([-6,6])
ax6.set_ylim([-6,6])
ax7.set_ylim([-6,6])
ax8.set_ylim([-6,6])

ax1.set_xlim([-5,5])
ax2.set_xlim([-5,5])
ax3.set_xlim([-5,5])
ax4.set_xlim([-5,5])
ax5.set_xlim([-5,5])
ax6.set_xlim([-5,5])
ax7.set_xlim([-5,5])
ax8.set_xlim([-5,5])

ax1.plot(x,y1)
ax2.plot(x,y2)
ax3.plot(x,y3)
ax4.plot(x,y3)
ax5.plot(x,y3)
ax6.plot(x,y3)
ax7.plot(x,y3)
ax8.plot(x,y3)

# axes = [[ ax1 ], [ ax2 ], [ ax3 ], [ ax4 ]] 
stick_axes(fig)
plt.show()
