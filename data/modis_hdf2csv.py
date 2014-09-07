#!/bin/python
# -*- coding: utf-8 -*-
from datetime import date, timedelta as td

if __name__ == "__main__":
    """ Download MODIS terra and aqua CMG active fire HDF files for a year 
        add them up and write to CSV """
        
        
    start = '201010'
    end   = '201012'

    for y in range(int(start[0:4]),int(end[0:4])+1):
        for m in range(int(start[4:]),int(end[4:])+1):
            print y,m
            ftp://fuoco.geog.umd.edu/modis/C5/cmg/monthly/hdf/
        
        
        