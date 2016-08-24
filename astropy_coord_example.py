#!/usr/bin/env python

import urllib
import IPython.display
import numpy as np

""""matplotlib inline"""
from matplotlib import pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table

#hcg7_center = SkyCoord(9.81625*u.deg, 0.88806*u.deg, frame='icrs')
#hg7_center
hcg7_center = SkyCoord.from_name('HCG 7')
hcg7_center

type(hcg7_center.ra), type(hcg7_center.dec)
hcg7_center.dec
hcg7_center.ra
hcg7_center.ra.hour

impix = 1024
imsize = 12*u.arcmin
cutoutbaseurl = 'http://skyservice.pha.jhu.edu/DR12/ImgCutout/getjpeg.aspx'
query_string = urllib.urlencode(dict(ra=hcg7_center.ra.deg,
                                     dec=hcg7_center.dec.deg,
                                     width=impix, height=impix,
                                     scale=imsize.to(u.arcsec).value/impix))

url = cutoutbaseurl + '?' + query_string

urllib.urlretrieve(url, 'HCG7_SDSS_cutout.jpg')

IPython.display.Image('HCG7_SDSS_cutout.jpg')


