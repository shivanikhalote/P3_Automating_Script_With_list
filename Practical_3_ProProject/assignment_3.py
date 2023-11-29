import arcpy

#setting Workspace
arcpy.env.workspace = r"C:\Users\shiva\Downloads\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists.gdb"
fc_list = arcpy.ListFeatureClasses()

buffer_dis = 0
for fc in fc_list:
    fc_obj = arcpy.Describe(fc)
    shape_type = fc_obj.ShapeType
# assigning buffer distance based on a feature class shape type
    if shape_type == "Point":
        buffer_dis = "300 meters"
    elif shape_type == "Polyline":
        buffer_dis = "500 meters"
    elif shape_type == "Polygon":
        buffer_dis = "700 meters"
    output_path = fc+"_Buffer"
# calculating buffer for each feature class
    arcpy.analysis.Buffer(fc,output_path,buffer_dis)



