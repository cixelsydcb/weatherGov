# -*- coding: utf-8 -*-

"""
weatherGov
=============================

"""

import requests, googlemaps
import defusedxml.ElementTree as ET

class Weather(object):
    """Basic class"""

    def setAPIKey(self, apiKey):
        self.clientKey = apiKey

    def getLatLong(self, address):
        """Call to get the lat and long returned as self.lat and self.long"""
        self.address = address
        gmaps = googlemaps.Client(key=self.clientKey)
        geocode_result = gmaps.geocode(self.address)
        results = dict(geocode_result[0])
        self.lat = str(results['geometry']['location']['lat'])
        self.long = str(results['geometry']['location']['lng'])
        

    def getCurWeather(self):
        """Call to get the current weather conditions from the weather.gov site
        sets up self.curConditions as an XML object

        """
        weatherUrl = 'http://forecast.weather.gov/MapClick.php?lat=' + self.lat + '&lon=' + self.long + '&unit=0&lg=english&FcstType=dwml'
        res = requests.get(weatherUrl)
        try:
            res.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % (exc))
        root = ET.fromstring(res.text)

        forecast = root.find("./data[@type='forecast']")
        timeLayout = forecast.find("./time-layout/layout-key")
        timeLayout = timeLayout.text
        searchString = "./parameters/wordedForecast[@time-layout='"+timeLayout+"']/text"
        self.curConditions = forecast.find(searchString)
