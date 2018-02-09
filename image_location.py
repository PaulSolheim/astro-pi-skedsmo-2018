#!/usr/bin/python3
import ephem
import picamera
import time
import datetime as dt
from math import degrees, radians, cos, sin, asin, sqrt

time_format = "%d/%m/%Y %H:%M:%S"

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   18015.76213144  .00002375  00000-0  42846-4 0  9998"
line2 = "2 25544  51.6430  58.5835 0003578  19.8447  92.3735 15.54313934 94810"

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

iss = ephem.readtle(name, line1, line2)

cam = picamera.PiCamera()
cam.annotate_background = picamera.Color('black')
cam.annotate_text_size = 50

target_lat = 53.349805
target_long = -6.260310

image_range = 208  # km

while True:
    iss.compute()
    iss_lat = degrees(iss.sublat)
    iss_long = degrees(iss.sublong)
    dist = haversine(iss_long, iss_lat, target_long, target_lat)
    print(dist)

    if dist < image_range:  # take pictures
        print("Target in range, taking picture")
        cam.start_preview()
        time.sleep(5)  # give time for camera to adjust to light level
        cam.annotate_text = dt.datetime.now().strftime(time_format)
        cam.capture("%s.jpg" % round(time.time()))
        cam.stop_preview()

    time.sleep(1)