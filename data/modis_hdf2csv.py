#!/bin/python
# -*- coding: utf-8 -*-

import ftplib 
import os.path
if __name__ == "__main__":
    """ Download MODIS terra and aqua CMG active fire HDF files for a year 
        add them up and write to CSV """
        
    ftp = ftplib.FTP('fuoco.geog.umd.edu')
    ftp.login(user='fire',passwd='burnt')
    ftp.cwd('modis/C5/cmg/monthly/hdf/')
    start = '201001'
    end   = '201012'

    for y in range(int(start[0:4]),int(end[0:4])+1):
        for m in range(int(start[4:]),int(end[4:])+1):
            
            filename = 'MOD14CMH.'+str(y)+str(m).zfill(2) + '.005.01.hdf'
            print filename
            if not os.path.exists('hdf/'+filename):
                localfile = open('hdf/'+filename, 'wb')
                ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
            
            filename = 'MYD14CMH.'+str(y)+str(m).zfill(2) + '.005.01.hdf'
            print filename
            if not os.path.exists('hdf/'+filename):
                localfile = open('hdf/'+filename, 'wb')
                ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
            
        
        
        