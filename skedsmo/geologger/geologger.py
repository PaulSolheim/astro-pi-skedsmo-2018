from sense_hat import SenseHat
from datetime import datetime

class GeoLogger:
    def __init__(self):
        self.sense = SenseHat()
        self.filename = "./logs/Geologg-"+str(datetime.now())+".csv"
        self.file_setup(self.filename)

    def write_line(self, line):
        with open(self.filename, "a") as f:
            f.write(line + "\n")
        
    def log_data(self):
        geo_data = self.get_geo_data()
        line = ",".join(str(value) for value in geo_data)
        self.write_line(line)

    def file_setup(self, filename):
        header = ["datetime", "image_filename", "geo_name", "type", "latitude", "longitude",
                  "iss_latitude", "iss_longitude", "distance", "compass"]

        with open(filename, "w") as f:
            f.write(",".join(str(value) for value in header)+ "\n")

    def find_compass(self):
        north = self.sense.get_compass()
        north = round(north, 1)
        
        return north
    
    def set_geo_data(self, image_filename, geo_name, type, latitude, longitude, iss_latitude, iss_longitude, distance):
        self.image_filename = image_filename
        self.geo_name = geo_name
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.iss_latitude = iss_latitude
        self.iss_longitude = iss_longitude
        self.distance = distance
        self.compass = self.find_compass()
        

    def get_geo_data(self):
        geo_data = []
        geo_data.append(datetime.now())
        geo_data.append(self.image_filename)
        geo_data.append(self.geo_name)
        geo_data.append(self.type)
        geo_data.append(self.latitude)
        geo_data.append(self.longitude)
        geo_data.append(self.iss_latitude)
        geo_data.append(self.iss_longitude)
        geo_data.append(self.distance)
        geo_data.append(self.compass)
        
        return geo_data
