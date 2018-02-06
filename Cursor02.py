#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jake MacLean
#
# Created:     06-02-2018
# Copyright:   (c) Jake MacLean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import os
scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)


import arcpy

fc = r"..\..\..\Data\Canada\Can_Mjr_Cities.shp"
fieldList = ["Name", "Prov"]
rowCount = 1
cursor = arcpy.da.SearchCursor(fc, fieldList)
rowCount = 1
for row in cursor:

    rowCount += 1

    fmt = "%s , %s"

    print fmt % (row[0],row[1])


print "There are", rowCount,"cities in the above list."

