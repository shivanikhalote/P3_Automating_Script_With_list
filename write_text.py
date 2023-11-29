import os
folder_path = r"C:\Users\shiva\Documents\programming_iii\P3_Automating_Script_With_list"
file_name = r"writeme.txt"

file_path = os.path.join(folder_path,file_name)

file_obj = open(file_path,'r+')

# read only ('r')
# read and write ('r+')
# write only ('w')
# read and write ('W+')
# append only ('a')
# append read read('a+')

input_text = "good afternoon everyone!!"
file_obj.write(input_text)
lines = file_obj.readlines()
for l in lines:
    print(l)
file_obj.close()


