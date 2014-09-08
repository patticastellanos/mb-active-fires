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

    fires = np.zeros((360,720),dtype=np.float64)
    #add up active fires for a year
    #download the data if needed
    for y in range(int(start[0:4]),int(end[0:4])+1):
        for m in range(int(start[4:]),int(end[4:])+1):
            modfilename = 'MOD14CMH.'+str(y)+str(m).zfill(2) + '.005.01.hdf'
            if not os.path.exists('hdf/'+modfilename):
                localfile = open('hdf/'+modfilename, 'wb')
                ftp.retrbinary('RETR ' + modfilename, localfile.write)
                localfile.close()
            
            mydfilename = 'MYD14CMH.'+str(y)+str(m).zfill(2) + '.005.01.hdf'
            if not os.path.exists('hdf/'+mydfilename):
                localfile = open('hdf/'+mydfilename, 'wb')
                ftp.retrbinary('RETR ' + mydfilename, localfile.write)
                localfile.close()
    #add up active fires for a year
    for y in range(int(start[0:4]),int(end[0:4])+1):
        for m in range(int(start[4:]),int(end[4:])+1):            
            # add up the active fires for the time range  
            mydfilename = 'MYD14CMH.'+str(y)+str(m).zfill(2) + '.005.01.hdf'
            print mydfilename
            mydfile = openhdf('hdf/'+mydfilename)                 
            mydfires= np.array((mydfile.SD.select('CloudCorrFirePix').get()),dtype=np.float64)           
            fires += mydfires.clip(0)

                          
            modfilename = 'MOD14CMH.'+str(y)+str(m).zfill(2) + '.005.01.hdf'
            print modfilename
            modfile = openhdf('hdf/'+modfilename)     
            modfires= np.array(modfile.SD.select('CloudCorrFirePix').get(),dtype=np.float64)
            fires += modfires.clip(0)

            
    #do some scaling to style
    fires = fires*100/fires.max()
    ff    = np.where(fires > 0.0)
    fm    = fires[ff].mean()
    ff    = np.where(fires > 3*fm)
    fires[ff] = 3*fm
    fires = fires*100/fires.max()
    #write the points to a csv
    csvfile = 'modis_fire_'+start+'_'+end+'.csv'
    f = open(csvfile,'w')
    f.write('latitude,longitude,fires\n')
    for ii,lat in enumerate(np.arange(90,-90,-0.5)):
        for jj,lon in enumerate(np.arange(-180,180,0.5)):
            if fires[ii,jj] > 0.0:
                outstring = '%f' %lat + ',%f' %lon + ',%f' %fires[ii,jj] + '\n'
                f.write(outstring)
    
    f.close()

        