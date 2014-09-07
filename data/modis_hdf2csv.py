#!/bin/python
# -*- coding: utf-8 -*-

import ftplib 
import os.path
from hdftools.openhdf import openhdf 
import numpy as np

if __name__ == "__main__":
    """ Download MODIS terra and aqua CMG active fire HDF files for a year 
        add them up and write to CSV """
        
    ftp = ftplib.FTP('fuoco.geog.umd.edu')
    ftp.login(user='fire',passwd='burnt')
    ftp.cwd('modis/C5/cmg/monthly/hdf/')
    start = '201001'
    end   = '201012'

    fires = np.zeros((360,720))
    #add up active fires for a year
    #download the data if needed
    for y in range(int(start[0:4]),int(end[0:4])+1):
        for m in range(int(start[4:]),int(end[4:])+1):
            
            modfilename = 'MOD14CMH.'+str(y)+str(m).zfill(2) + '.005.01.hdf'
            if not os.path.exists('hdf/'+modfilename):
                localfile = open('hdf/'+modfilename, 'wb')
                ftp.retrbinary('RETR ' + modfilename, localfile.write, 1024)
            
            mydfilename = 'MYD14CMH.'+str(y)+str(m).zfill(2) + '.005.01.hdf'
            if not os.path.exists('hdf/'+mydfilename):
                localfile = open('hdf/'+mydfilename, 'wb')
                ftp.retrbinary('RETR ' + mydfilename, localfile.write, 1024)
                
            # add up the active fires for the time range
            print 'hdf/'+mydfilename
            mydfile = openhdf('hdf/'+mydfilename)       
            mydfires= mydfile.SD.select('CloudCorrFirePix')
            fires   += mydfires.get()
            

        