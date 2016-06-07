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


def stick_axes(fig):
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
    l_axes = fig.axes
    print(l_axes)
    nrows, ncols, _, _ = l_axes[0].get_subplotspec().get_geometry()
    print(nrows, ncols)
    axes = [[0 for j in range(ncols)] for i in range(nrows)]
    for ax in l_axes:
        _, _, ind, _ = ax.get_subplotspec().get_geometry()
        row, col = ind//ncols, ind%ncols
        print ind, row, col
        axes[row][col] = ax
    # n_count = 0
    # for i in range(nrows):
    #     aux = []
    #     for j in range(ncols):
    #         aux.append(l_axes[n_count])
    #         n_count += 1
    #     axes.append(aux)
    # Se mira si es un vector y se convierte en array para que todo sea consistente
    # if type(axes[0]) is not list:
    #     axes = [axes]
    # Se leen el número de filas y de columnas
    # nrows = len(axes)
    # ncols = len(axes[0])
    # Se quita el interespaciado
    plt.subplots_adjust(hspace=0.001)
    plt.subplots_adjust(wspace=0.001)
    # Se eliminan las etiquetas que queden en los intersticios
    # Primero en x
    print(axes)
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
