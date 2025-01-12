import os

def func_to_write_data_into_txt(data, var = 1):
    file_name = open(f"D:\\My_docs\python\\learning\\4_Python_modules\\OS_module\\os_data.txt","a+")
    write_data = str(data)
    if var == 1:
        for i in write_data:
            file_name.write(i)
    else:
        pass
    file_name.write("\n")

#provides the list of the all the functions and variables available in the Os module
func_to_write_data_into_txt(dir(os))
#provides the path of the current working directory
func_to_write_data_into_txt(os.getcwd())
#Changes the current working directory 
func_to_write_data_into_txt(os.chdir("D:\\My_docs\\python\\learning\\4_Python_modules"))
func_to_write_data_into_txt()