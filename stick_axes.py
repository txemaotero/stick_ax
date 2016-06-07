#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Descripción:

Se define una función para juntar los ejes de una figura
'''
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator # added 
import numpy as np


def stick_axes(axes):
    """
    Stick the axes of a figure. 'axes' is a list of list with the axes.
    It could also be a list of axes.

    Parameters:
    -----------
    axes : list
        e.g. axes = [[ax1, ax2], [ax3, ax4]]
        In this case, x_axes of ax1-ax3 and ax2-ax4 are stick and the same to
        y_axes for ax1-ax2 and ax3-ax4.
        ax1 is supposed to be in the top-left corner.
    """
    # Se mira si es un vector y se convierte en array para que todo sea consistente
    if type(axes[0]) is not list:
        axes = [axes]
    # Se leen el número de filas y de columnas
    nrows = len(axes)
    ncols = len(axes[0])
    # Se quita el interespaciado
    plt.subplots_adjust(hspace=0.001)
    plt.subplots_adjust(wspace=0.001)
    # Se eliminan las etiquetas que queden en los intersticios
    # Primero en x
    if nrows > 1:
        for i in range(nrows-1):
            for j in range(ncols):
                axes[i][j].set_xticklabels([])
    # Ahora en y
    if ncols > 1:
        for j in range(ncols-1):
            for i in range(nrows):
                axes[i][j+1].set_yticklabels([])
    # Se eliminan las etiquetas que solapan
    # En x
    if ncols > 1:
        nbins = len(axes[-1][-1].get_xticklabels())
        for j in range(nrows):
            for i in range(ncols-1):
                axes[j][i].xaxis.set_major_locator(MaxNLocator(nbins=nbins, prune='upper'))
    # En y
    if nrows > 1:
        nbins = len(axes[-1][0].get_xticklabels())
        for i in range(nrows-1):
            for j in range(ncols):
                axes[i+1][j].yaxis.set_major_locator(MaxNLocator(nbins=nbins, prune='upper'))
        # plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

x = np.linspace(-5,5,100)
y1 = np.cos(x)
y2 = x**2
y3 = x
y4 = x+3
y5 = x*0 -1

ax1.set_ylim([-6,6])
ax2.set_ylim([-6,6])
ax3.set_ylim([-8.5,7.5])
ax4.set_ylim([-8.5,7.5])

ax1.set_xlim([-5,5])
ax2.set_xlim([-5,5])
ax3.set_xlim([-5,5])
ax4.set_xlim([-5,5])

ax1.plot(x,y1)
ax2.plot(x,y2)
ax3.plot(x,y3)
ax4.plot(x,y3)

# ax2.xaxis.set_ticks(ax1.xaxis.get_major_ticks())
# print(ax1.xaxis.get_ticks_position())

print(matplotlib.ticker.Locator)
axes = [[ax1, ax2], [ax3, ax4]]
stick_axes(axes)
plt.show()
