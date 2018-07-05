# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import numpy as np
from topopy import DEM, Flow, Network
import matplotlib.pyplot as plt

#infolder = "data/in/"
#outfolder = "data/out/"
#
#files = ['tunez.tif', 'small25.tif', 'jebja30.tif']
#
#for file in files:
#    dem = DEM(infolder + file)
#    fill = dem.fill_sinks()
#    fill.save("{0}fill_{1}".format(infolder, file))
#    fd = Flow(dem)
#    fd.save_gtiff("{0}fd_{1}".format(infolder, file))
#    fd = Flow(dem, auxtopo=True)
#    fd.save_gtiff("{0}fd2_{1}".format(infolder, file))
#
##dem = DEM(infolder + "jebja30.tif")
##fd = Flow(dem)
##fd.save_gtiff(outfolder + "fd_test.tif")
##fac = fd.get_flow_accumulation()
##fac.save(outfolder + "fac.tif")
##
##net = Network(fd, 1000)
##outlets = net.get_stream_poi("outlets")
##x, y = net.cell_2_xy(outlets[0], outlets[1])
##xy = np.array((x, y)).T
##
##basins = fd.get_drainage_basins([x, y])
##basins.save(outfolder + "basins.tif")
##
##np.savetxt(outfolder +  "outlets.txt", xy, delimiter=";")
##streams = net.get_streams()
##streams.save(outfolder + "streams.tif")

from topopy.ext import sortcells as sc
dem = DEM("data/in/small.tif")
fd = Flow(dem)
net = Network(fd, dem, 3)

net.calculate_chi()