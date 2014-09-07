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
                ftp.retrbinary('RETR ' + modfilename, localfile.write)
                localfile.close()
            
            mydfilename = 'MYD14CMH.'+str(y)+str(m).zfill(2) + '.005.01.hdf'
            if not os.path.exists('hdf/'+mydfilename):
                localfile = open('hdf/'+mydfilename, 'wb')
                ftp.retrbinary('RETR ' + mydfilename, localfile.write)
                localfile.close()
    
    for y in range(int(start[0:4]),int(end[0:4])+1):
        for m in range(int(start[4:]),int(end[4:])+1):            
            # add up the active fires for the time range
            print mydfilename  
            mydfile = openhdf('hdf/'+mydfilename)                 
            mydfires= mydfile.SD.select('CloudCorrFirePix').get()            
            ff = np.where(mydfires > 0)
            fires[ff] = fires[ff] + mydfires[ff]
            
            print modfilename  
            modfile = openhdf('hdf/'+modfilename)     
            modfires= modfile.SD.select('CloudCorrFirePix').get()  
            ff = np.where(modfires > 0)
            fires[ff] = fires[ff] + modfires[ff]
    
    fires = fires*100/fires.max()
    ff    = np.where(fires > 0)
    fm    = fires[ff].mean()
    ff    = np.where(fires > 3*fm)
    fires[ff] = 3*fm
    #write the points to a csv
    csvfile = 'modis_fire_'+start+'_'+end+'.csv'
    f = open(csvfile,'w')
    f.write('latitude,longitude,fires\n')
    for ii,lat in enumerate(np.arange(90,-90,-0.5)):
        for jj,lon in enumerate(np.arange(-180,180,0.5)):
            if fires[ii,jj] > 0:
                outstring = '%f' %lat + ',%f' %lon + ',%f' %fires[ii,jj] + '\n'
                f.write(outstring)
    
    f.close()

        