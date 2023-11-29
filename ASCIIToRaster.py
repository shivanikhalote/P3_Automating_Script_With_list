import arcpy
input_asc = r"C:\Users\shiva\Downloads\prac 2 data and software (1)\prac 2 data and software\micro_output\microryzomys_minutus_avg.asc"
output_raster = r"C:\Users\shiva\Documents\ArcGIS\Projects\maxent\maxent.gdb\raster"
datatype = "FLOAT"
arcpy.ASCIIToRaster_conversion(input_asc,output_raster,datatype)