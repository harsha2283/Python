def write_data_to_func():
    #open a file for writing and reading the data
    my_file = open("text_file.txt","w")

    #write some lines of data to the file 
    for i in range (10):
        my_file.write(f"write the below text in to the file {i}\n")
    
    #closing the file 
    my_file.close()

def reading_the_data_from_text_file():
    #opening the file in the read mode 
    my_file = open("text_file.txt","r")

    #Reading the data from the file in a wholesome
    if my_file.mode == "r":
        contents = my_file.read()
        print(contents)
    
    #closing the file 
    my_file.close()

    #opening the file in the read mode 
    my_file = open("text_file.txt","r")

    #Reading the data from the file line by line
    if my_file.mode == "r":
        file_line = my_file.readlines()
        for x in file_line:
            print(x)
    
    #closing the file 
    my_file.close()

write_data_to_func()
reading_the_data_from_text_file()


    