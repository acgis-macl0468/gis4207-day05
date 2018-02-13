#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      thowl
#
# Created:     13-02-2018
# Copyright:   (c) thowl 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Placemark>
    <name>Simple placemark</name>
    <description>Attached to the ground. Intelligently places itself
       at the height of the underlying terrain.</description>
    <Point>
      <coordinates>-122.0822035425683,37.42228990140251,0</coordinates>
    </Point>
  </Placemark>
</kml>

import os
scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)


import arcpy

rows = arcpy.SearchCursor(r"..\..\..\Data\Canada\Can_Mjr_Cities.shp",
                          Prov ="ON",
                          ""
                          "Name; Prov")

print "Name, Prov"
n = 1
for row in rows:
    n += 1
    fmt = "%s , %s"
    print fmt % (row.Name, row.Prov)

print "There are", n,"cities in the above list."