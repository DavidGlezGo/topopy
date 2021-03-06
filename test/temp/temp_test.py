#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:53:42 2018

@author: vicen
"""

from topopy import Flow, Network, DEM
import numpy as np
import matplotlib.pyplot as plt

# Get DEM, Flow and Network
dem = DEM("../data/in/jebja30.tif")
fd = Flow(dem)
net = Network(dem, fd, 1000)

# Head
x = 577413
y = 496519
row, col = fd.xy_2_cell(x, y)
ix = fd.cell_2_ind(row, col)

def get_channel(fd, ix):
    ixcix = np.zeros(fd._ncells, np.int)
    ixcix[fd._ix] = np.arange(len(fd._ix))
    channel_points = [ix]
    new_ind = ix
    while ixcix[new_ind] != 0:
        new_ind = fd._ixc[ixcix[new_ind]]
        channel_points.append(new_ind)
    return channel_points

def get_channel2(net, ix):
    channel = [ix]
    while ix.size > 0:
        idx = np.where(net._ix == ix)
        if idx[0].size == 0:
            break
        channel.append(int(net._ixc[idx]))
        ix = net._ixc[idx]
            
    return channel

## Testing method 01
#marr = np.zeros(fd._ncells, np.int)
#channel_points = get_channel(fd, ix)
#marr[channel_points] = 1
#marr = marr.reshape(fd._dims)
#fig, ax = plt.subplots()
#ax.imshow(marr)
#
# Testing method 02
marr = np.zeros(fd._ncells, np.int)
channel_points = get_channel2(net, ix)
marr[channel_points] = 1
marr = marr.reshape(fd._dims)
fig2, ax2 = plt.subplots()
ax2.imshow(marr)
    
def test_01(dem, fd):
    for n in range(100):
        row = np.random.randint(0, dem.get_dims()[0])
        col = np.random.randint(0, dem.get_dims()[1])
        ix = fd.cell_2_ind(row, col)
        get_channel(fd, ix)
        
        
def test_02(dem, net):
#    marr = np.zeros(fd._ncells, np.int)
    for n in range(100):
        ix = np.random.choice(net._ix)
        get_channel2(net, ix)
#        marr[ch_points] = 1
    
#    marr = marr.reshape(fd._dims)
#    fig2, ax2 = plt.subplots()
#    ax2.imshow(marr)    
#    
        
        
        
        