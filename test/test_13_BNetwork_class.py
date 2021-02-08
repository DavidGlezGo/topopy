#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 26 march, 2020 (COVID19 quarantine)
Testing suite for BNetwork class
@author: J. Vicente Perez
@email: geolovic@hotmail.com
@date: 26 march, 2020 (COVID19 quarantine)
"""

import unittest
import numpy as np
import os
from topopy import Flow, Basin, Network, BNetwork, DEM
infolder = "data/in"
outfolder = "data/out"

class BNetworkClassTest(unittest.TestCase):
    
    def test_BNetworkClass(self):
        files = ["small25", "jebja30", "tunez"]
        print("Executing test for BNetwork class...")
        for file in files:
            # Cargamos DEM, Flow, Network
            fd = Flow("{}/{}_fd.tif".format(infolder, file))
            net = Network("{}/{}_net.dat".format(infolder, file))
            dem = DEM("{}/{}.tif".format(infolder, file))
            
            # Generamos todas las cuencas
            cuencas = fd.get_drainage_basins(min_area = 0.0025)
            
            # Generamos 50 puntos aleatorios dentro de la extensión del objeto Network
            # Estos 50 puntos se usaran como cabeceras
            xmin, xmax, ymin, ymax = net.get_extent()
            xi = np.random.randint(xmin, xmax, 50)
            yi = np.random.randint(ymin, ymax, 50)
            heads = np.array((xi, yi)).T
            
            # Cogemos 5 cuencas aleatorias
            bids = np.random.choice(np.unique(cuencas.read_array())[1:], 5)
            print("Test with DEM: ", file)
            for bid in bids:
                if np.random.randint(101) < 70:
                    print("Creating BNetwork from grid, file = {}, bid={}".format(file, bid))
                    bnet = BNetwork(net, cuencas, heads, bid)
                else:
                    print("Creating BNetwork from Basin, file = {}, bid={}".format(file, bid))
                    basin = Basin(dem, cuencas, bid)
                    bnet = BNetwork(net, basin, heads, bid)
                
                # Salvamos BNetwork y volvemos a cargar para comprobar que se cargan-guardan bien
                bnet_path = "{}/{}_{}_bnet.dat".format(outfolder, file, bid)
                bnet.save(bnet_path)
                bnet2 = BNetwork(bnet_path)
                computed = np.array_equal(bnet._ix, bnet2._ix)
                self.assertEqual(computed, True)
                # borramos archivo
                os.remove(bnet_path)


if __name__ == "__main__":
    unittest.main()