import arcpy
arcpy.env.workspace = r"C:\Users\shiva\Downloads\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb"

file_list = arcpy.ListFeatureClasses()

for name in file_list:
    print(name)

print(" ")

field_list = arcpy.ListFields("Freeways")

for field in field_list:
    print(field.name)
    print(field.type)
    print(field.length)
    print("-----------------------")



