import datetime, time
import ephem
import math

name = "ISS (ZARYA)"             
line1 = "1 25544U 98067A   18018.53557894  .00043896  00000-0  66473-3 0  9993"
line2 = "2 25544  51.6423  44.7554 0003536  21.4730 139.6427 15.54204895 95241"

iss = ephem.readtle(name, line1, line2)

# find if we are in night or daytime
sun = ephem.Sun()
twilight = math.radians(-6)

while True:
    try:
        now = datetime.datetime.utcnow()
        iss.compute(now)
        
        obs = ephem.Observer()
        obs.lat = iss.sublat
        obs.long = iss.sublong
        obs.elevation = 0
        
        sun.compute(obs)
        sun_angle = math.degrees(sun.alt)
        day_or_night = "Day" if sun_angle > twilight else "Night"
        
        ### transform longitude and latitude to degrees
        print("longitude: %s - latitude: %s - %s" % (math.degrees(iss.sublong), math.degrees(iss.sublat), day_or_night))
    ### catch the exceptions
    except Exception as inst:
        print("Feil")

    #Sleep 30 seconds
    time.sleep( 30 )
    