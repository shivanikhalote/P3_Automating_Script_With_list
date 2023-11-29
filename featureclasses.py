import arcpy

arcpy.env.workspace = r"C:\Users\shiva\Documents\programming_iii\P3_Automating_Script_With_list\Practical_3_ProProject\Practical_3_ProProject\03_Automating_Scripts_With_Lists.gdb"

fc_list = arcpy.ListFeatureClasses()

buffer_distance = 0
for fc in fc_list:
    desc_obj = arcpy.Describe(fc)
    shape_type = desc_obj.shapeType


    # point: 500 feet, polyline: 1000 feet, polygon: 600 feet

    if shape_type == "Point":
        buffer_distance = "500 feet"
    elif shape_type == "Polyline":
        buffer_distance = "1000 feet"
    elif shape_type == "Polygon":
        buffer_distance = "600 feet"
    output_buffer = fc + "_Buffer"
    arcpy.analysis.Buffer(fc, output_buffer, buffer_distance)


