import arcpy
import os

arcpy.env.workspace = r"C:\Users\shiva\Downloads\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb"
folder_path = r"C:\Users\shiva\Documents\programming_iii\P3_Automating_Script_With_list"
output_file_name = "field_info.txt"

output_file_path = os.path.join(folder_path,output_file_name)

file_obj = open(output_file_path,'w')
fc_obj = arcpy.ListFeatureClasses()
for name in fc_obj:
    print(name)
    file_obj.write(name + "\n")

    field_obj = arcpy.ListFields(name)
    for field in field_obj:
        print("Field_name: {}, field_type: {}, field_length: {}\n".format(field.name,field.type,field.type))
        file_obj.write("Field_name: {}, field_type: {}, field_length: {}\n".format(field.name,field.type,field.type))
        print("--------------------------------------------------------------------")
        file_obj.write("--------------------------------------------------------------------\n")
