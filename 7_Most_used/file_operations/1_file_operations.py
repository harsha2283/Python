
list_of_data_to_be_written_to_the_file = ["This","data","is","written","into","the","file","from","writelines()","function"]

#file oeprations 
with open("output.txt", "w") as file:
    #writting data i
    print("This data is written into the file using a print function",file=file)
    file.write("This line is written in to this file using write function\n")
    file.writelines(list_of_data_to_be_written_to_the_file)

help(file.writelines)