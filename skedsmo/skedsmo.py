# import libraries
from sense_hat import SenseHat
from datetime import datetime, timedelta
import time
from senselogger import SenseLogger
from geologger import GeoLogger
from dataaccess import DataAccess
from orbmatcher import ORBMatcher
import animation
import text
import cv2
import picamera
import os
import ephem
from math import degrees, radians, cos, sin, asin, sqrt, pi
import random

name = "ISS (ZARYA)"             
line1 = "1 25544U 98067A   18035.94876567  .00002435  00000-0  44124-4 0  9992"
line2 = "2 25544  51.6419 317.9464 0003249  74.7289  17.1572 15.54056069 97951"

iss = ephem.readtle(name, line1, line2)

# Set lower to save storage space
# Using cirka 300 MB in 3 hours with this resolution
res_x = 2592
res_y = 1944    # correct for V1 camera on ISS

image_range = 208  # km

# Set to False to disable feature matching
# When set to false images in the training folder is not needed
# and less images are stored (cirka 50-70 less images saving cirka 8 MB storage space
do_feature_matching = False

###  Define Functions  ###

def capture_image():
    timeStamp = time.strftime("%d-%m-%Y_%H:%M:%S")
    # Add timestamp to filename
    filename = ('logs/images/img_%s.jpg' % timeStamp)
    # Capture and save image   
    camera.capture(filename)
    return filename


def haversine(lat1, lon1, lat2, lon2):
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
    r = 6371 # Radius of earth in kilometers.
    return c * r


def get_position_and_time():
    try:
        now = datetime.utcnow()
        iss.compute(now)
        
        obs = ephem.Observer()
        obs.lat = iss.sublat
        obs.long = iss.sublong
        obs.elevation = 0
        
        sun.compute(obs)
        sun_angle = degrees(sun.alt)
        daytime = True if sun_angle > twilight else False
        
        ### transform longitude and latitude to degrees
        long = degrees(iss.sublong)
        lat = degrees(iss.sublat)

    ### catch the exceptions
    except Exception as ex:
        print("Error in get_position_and_time")
        print(ex)
        
    return long, lat, daytime

###  Main Program  ###

# initialize variables
sense = SenseHat()
sense.set_rotation(270)

# initialize camera
camera = picamera.PiCamera()
camera.hflip = False
camera.resolution = (res_x, res_y)
time.sleep(3)  # give time for camera to adjust to light level

# to be able to find if we are in night or daytime
sun = ephem.Sun()
twilight = radians(-6)

# initialize text
text.init_text()

# initialize loggers
senselogger = SenseLogger()
geologger = GeoLogger()

# initialize dataaccess
dataaccess = DataAccess()

# initialize ORBMatcher
orbmatcher = ORBMatcher()

# set timedelta between each photo
time_between = timedelta(seconds=30)
loop_counter = 0

while True:
    # take a photo and save to log directory
    filename = capture_image()
    # print(filename)
    last_photo_time = datetime.now()
    
    longitude, latitude, isDaytime = get_position_and_time()
    # print("longitude: %s - latitude: %s - %s" % (longitude, latitude, isDaytime))
    
    # Log raw sensordata to senselogg
    senselogger.log_data()
    
    # Annotation Flag
    annotated = False
    # Feature Matching Flag
    matched = False
    
    try:
        # find mountains
        rows = dataaccess.get_mountains(latitude, longitude)
        for row in rows:
            geo_name = row[0]
            target_long = row[1]
            target_lat = row[2]
            distance = haversine(latitude, longitude, target_lat, target_long)
            if distance < image_range:
                # Write to geologg
                geologger.set_geo_data(filename, geo_name, "M", target_lat, target_long, latitude, longitude, distance)
                geologger.log_data()
                # print("geologging Mountain")
                annotated = True
                
            # print(row[0] + " long: " + str(row[1]) + " lat: " + str(row[2]))
            
        # find cities
        rows = dataaccess.get_cities(latitude, longitude)
        for row in rows:
            geo_name = row[0]            
            target_long = row[3]
            target_lat = row[2]
            distance = haversine(latitude, longitude, target_lat, target_long)
            if distance < image_range:
                # Write to geologg
                geologger.set_geo_data(filename, geo_name, "C", target_lat, target_long, latitude, longitude, distance)
                geologger.log_data()                
                # print("geologging City")
                annotated = True
                
            # print(row[0] + " long: " + str(row[3]) + " lat: " + str(row[2]))
            
    ### catch the exceptions
    except Exception as ex:
        print("Error in dataaccess get_mountains or get_cities")
        print(ex)            
            
    if isDaytime:
        if do_feature_matching:
            # Do feature mapping on raw image versus google engine image
            # as an option, if we are allowed to ship images with the code.
            # We are using the ORB algoritm included with OpenCV.
            
            training_filename = ""
            training_distance = 90
            try:
                # find training, pick the one with closest latitude
                rows = dataaccess.get_training(latitude, longitude)
                for row in rows:
                    training_id = row[0]
                    training_latitude = row[1]
                    training_longitude = row[2]
                    if (training_latitude - latitude) < training_distance:
                        training_distance = training_latitude - latitude
                        training_filename = "training/img_" + training_id + "_" + str(int(round(training_latitude))) + "_" + str(int(round(training_longitude))) + ".jpg"
                        
                    # print("id: " + row[0] + " " + str(row[1]) + " " + str(row[2]))

            ### catch the exceptions
            except Exception as ex:
                print("Error in dataaccess get_training")
                print(ex)
            
            # if we found a training image then do matching
            if training_filename != "":
                try:
                    # print("training filename: " + training_filename)
                    orbmatcher.match(training_filename, filename)
                    matched = True
                    
                ### catch the exceptions
                except Exception as ex:
                    print("Error in orbmatcher match")
                    print(ex)

    # Delete image if no annotation or match to save storage space
    # There should be no cities, mountains or training images (in daytime) for this image
    if not (annotated or matched):
        try:
            # delete image file
            os.remove(filename)
            
        ### catch the exceptions
        except Exception as ex:
            print("Error in delete image file")
            print(ex)
            
    # Show Text
    text.show_text()
    
    # Show Animation
    animation.show_animation()
    
    time_now = datetime.now()
    loop_counter = loop_counter + 1
    print("Round: " + str(loop_counter))
    if time_now < (last_photo_time + time_between):
        # We have to wait some seconds to get 30 seconds between pictures
        sleepSecs = (last_photo_time + time_between) - time_now
        print("Sleeping: " + str(sleepSecs.total_seconds()))
        
        time.sleep(sleepSecs.total_seconds())
    
