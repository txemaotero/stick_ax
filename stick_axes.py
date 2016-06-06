#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Descripción:

Se define una función para juntar los ejes de una figura
'''


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
    """
