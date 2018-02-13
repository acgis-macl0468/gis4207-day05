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

import os
scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)


import arcpy

rows = arcpy.SearchCursor(r"..\..\..\Data\Canada\Can_Mjr_Cities.shp",
                          Prov ="ON",
                          ""
                          "Name; Prov, x")

print "Name, Prov"
n = 1
for row in rows:
    n += 1
    fmt = "%s , %s"
    print fmt % (row.Name, row.Prov, row.shape.firstPoint.x)

print "There are", n,"cities in the above list."