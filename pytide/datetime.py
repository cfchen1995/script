#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Changfu Chen, Southwest Jiaotong University
# June 20, 2017
# 

from math import *

# ====================================================================
# datetime package
# --------------------------------------------------------------------
# Subroutine: Gregorian Calendar to Julian Date.
# --------------------------------------------------------------------
def cal2jd(iy,im,id):
    # Function:
    #       Gregorian Calendar to Julian Date.
    # Input:
    #       iy,im,id: year, month, day in Gregorian calendar
    # Output:
    #       djm0: MJD zero-point, always is 2400000.5
    #       djm: Modified Julian Date for 0 hours
    # Example:
    #       iy=2016;im=5;id=28;
    #       [djm0,djm,j] = cal2jd(iy,im,id);
    # Results:
    #       djm=57536;
    iymin = -4799
    mtab = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    j = 0
    if ( iy < iymin ):
        j = -1
        print('Bad year! JD not computed.')
    else:
        if (im < 1 or im > 12):
            j=-2
            print('Bad month! JD not computed.')
        else:
            ly = ((im == 2) and (not (iy%4)) and ((iy%100) or not (iy%400)))
            if ( (id < 1) or (id > (mtab[im-1] + ly))):
                j = -3
                print('Bad day! JD computed.')
            else:
                my = int((im-14)/12)
                iypmy = iy + my
                djm0 = 2400000.5
                djm = int((1461*(iypmy+4800))/4) \
                    + int((367*(im-2-12*my))/12) \
                    - int((3*((iypmy+4900)/100))/4) \
                    + id - 2432076
            
        
    
    return djm0,djm,j
    
# --------------------------------------------------------------------
# Subroutine: Calculate delta(AT) = TAI -UTC for a given UTC date.
# --------------------------------------------------------------------
def dat(iy,im,id,fd):
    # Function:
    #       Calculate delta(AT) = TAI -UTC for a given UTC date.
    #       Latest leap second: June 30, 2015
    # Input:
    #       iy, im, id, fd: UTC date of year, month, day, fraction of day
    # Output:
    #       deltat: TAI minus UTC, seconds
    
    # Release year for this version of dat
    IYV = 2015
    
    # Reference dates (MJD) and drift rates (s/day), pre leap seconds
    drift = [[37300.0, 0.0012960],
             [37300.0, 0.0012960],
             [37300.0, 0.0012960],
             [37665.0, 0.0011232],
             [37665.0, 0.0011232],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [39126.0, 0.0025920],
             [39126.0, 0.0025920]]
    
    # Number of Delta(AT) expressions before leap seconds were introduced 
    NERA1 = len(drift)
    
    # iyear month  Delta(AT)
    changes = [[1960,  1,  1.4178180],
               [1961,  1,  1.4228180],
               [1961,  8,  1.3728180],
               [1962,  1,  1.8458580],
               [1963, 11,  1.9458580],
               [1964,  1,  3.2401300],
               [1964,  4,  3.3401300],
               [1964,  9,  3.4401300],
               [1965,  1,  3.5401300],
               [1965,  3,  3.6401300],
               [1965,  7,  3.7401300],
               [1965,  9,  3.8401300],
               [1966,  1,  4.3131700],
               [1968,  2,  4.2131700],
               [1972,  1, 10.0      ],
               [1972,  7, 11.0      ],
               [1973,  1, 12.0      ],
               [1974,  1, 13.0      ],
               [1975,  1, 14.0      ],
               [1976,  1, 15.0      ],
               [1977,  1, 16.0      ],
               [1978,  1, 17.0      ],
               [1979,  1, 18.0      ],
               [1980,  1, 19.0      ],
               [1981,  7, 20.0      ],
               [1982,  7, 21.0      ],
               [1983,  7, 22.0      ],
               [1985,  7, 23.0      ],
               [1988,  1, 24.0      ],
               [1990,  1, 25.0      ],
               [1991,  1, 26.0      ],
               [1992,  7, 27.0      ],
               [1993,  7, 28.0      ],
               [1994,  7, 29.0      ],
               [1996,  1, 30.0      ],
               [1997,  7, 31.0      ],
               [1999,  1, 32.0      ],
               [2006,  1, 33.0      ],
               [2009,  1, 34.0      ],
               [2012,  7, 35.0      ],
               [2015,  7, 36.0      ]]
    
    # Number of Delta(AT) changes 
    NDAT = len(changes)
    
    # If invalid fraction of a day, set error status and give up. 
    if (fd < 0 or fd > 1):
        print('invalid fraction of a day')
    
    
    # Convert the date into an MJD. 
    [djm0, djm, j] = cal2jd(iy, im, id)
    
    # If pre-UTC year, set warning status and give up. 
    if (iy < changes[0][0]):
        print('pre-UTC year')
    
    
    # If suspiciously late year, set warning status but proceed. 
    if (iy > IYV + 5):
        print('suspiciously late year')
    
    
    # Combine year and month to form a date-ordered integer... 
    m = 12*iy + im
    
    # ...and use it to find the preceding table entry.
    for i in range(NDAT,1,-1):
        if (m >= (12 * changes[i-1][0] + changes[i-1][1])): 
            break
        
    
    
    # Get the Delta(AT)
    da = changes[i-1][2]
    
    # If pre-1972, adjust for drift
    if ((i-1) < NERA1):
        da = da + (djm + fd - drift[i-1][0]) * drift[i-1][1]
    
    
    # Return the Delta(AT) value
    deltat = da
    return deltat
    
# datetime package
# ====================================================================