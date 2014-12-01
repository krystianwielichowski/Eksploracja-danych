import arcpy
from numpy import corrcoef

fc = "D:/Wielichowski/ekploracja/bdo/powiaty.shp"

rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc, "", "String")

powierzchnia = []
ludnosc = []

for row in rows:
    powierzchnia.append(row.getValue("POLE_KM2"))
    ludnosc.append(row.getValue("POP"))


print corrcoef(powierzchnia, ludnosc)[0,1]
