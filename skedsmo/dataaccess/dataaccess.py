import sqlite3
from sqlite3 import Error


class DataAccess:
    def __init__(self):
        self.database = "database.db"
        self.create_connection()

    def create_connection(self):
        """ create a database connection to the SQLite database
        """
        try:
            self.conn = sqlite3.connect(self.database)
        except Error as e:
            self.conn = None
            print(e)
   
    def get_mountains(self, lat, long):
        """
        Query Mountains near Latitude/Longitude
        :param lat: the latitude
        :param long: the longitude
        :return: rows with mountains
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM mountains where lat>? AND lat<? AND lng>? AND lng<?", (lat-2, lat+2, long-3, long+3,))

        rows = cur.fetchall()

        return rows

    def get_cities(self, lat, long):
        """
        Query Mountains near Latitude/Longitude
        :param lat: the latitude
        :param long: the longitude
        :return: rows with cities
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM cities where lat>? AND lat<? AND lng>? AND lng<?", (lat-2, lat+2, long-3, long+3,))

        rows = cur.fetchall()

        return rows

    def get_training(self, lat, long):
        """
        Query Training image with Latitude/Longitude
        :param lat: the latitude
        :param long: the longitude
        :return: rows with training image if exists,
        may return more than one row because of
        overlap in training images
        """
        
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM training where (center_long < (? + (nr_of_longs / 2))) AND (center_long > (? - (nr_of_longs / 2))) AND (center_lat < (? + (nr_of_lats / 2))) AND (center_lat > (? - (nr_of_lats / 2)))", (long, long, lat, lat,))
        
        rows = cur.fetchall()
        
        return rows
    