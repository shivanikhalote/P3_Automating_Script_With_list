import arcpy

# giving point feature path to variable point_path
point_path = r"C:\Users\shiva\Documents\ArcGIS\Projects\Point_buffer\Point_buffer.gdb\point"

# creating output file of 500 meter buffer using concatenation in file name
output_buffer = point_path + "_500m_buffer"
buffer_distance = "500 meters"
arcpy.analysis.Buffer(point_path, output_buffer, buffer_distance)

# initilating multiple buffer list which contain sets of buffer range to calculate buffer
multi_buffer = ["1000 feet","1200 feet","1400 feet"]

range = 1000
for buf in multi_buffer:

    # replace() function is use to
    output_multi_buffer = point_path + "_" + str(range) + "_feet_buffer"
    arcpy.analysis.Buffer(point_path, output_multi_buffer, buf)
    range += 200
print("process_complete")








