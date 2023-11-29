import os
folder_path = r"C:\Users\shiva\Documents\programming_iii\P3_Automating_Script_With_list"
file_name = r"readme.txt"

file_path = os.path.join(folder_path,file_name)
file_obj = open(file_path, 'r')
#print(file_obj.read())
# print("first 5 characters from file is {} ".format(file_obj.read(5)))
# print(file_obj.readlines())

count = 0
lines = file_obj.readlines()

for line in lines:
    count += 1
    print("{} {}".format(count,line))




