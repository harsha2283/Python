#-------------------------------------------------------------------------------------#
#................. concepts are learnt from ..........................................#
# https://www.youtube.com/watch?v=bnSYeYFRCaA&list=PL4KX3oEgJcffJTxggH5LviQeMHiNagq3y #
#.....................................................................................#                                                                                
#-------------------------------------------------------------------------------------#

array_of_strings = ["hELLo", "MARIo", "center", "RTE_core0_RTE_core1_RTE_core2_RTE_core3", "starter", "text\ttext\ttext", "we can create multiple instances of a class",
                    "{} name is {}", "{type} name is {Character}", "mapping is done to the string using format_map() {class} -> {instance}", "password@123", "password123",
                     "123", "Var_name","lower",'  ',"The Gladiator", "the Gladiator","_","tail_text", "UPPER_TO_LOWER", "Butterfly - Butterfly","A=B=C", "content invalid",
                     "be a wise man to be wise","Master String", "lower_to_upper","zfill"]

# creating dictionary 
translate = {"B":"@","t":"#"}

string_methods_dict = dict()
#1 capitalize()
string_methods_dict["capitalize"] = (array_of_strings[0].capitalize())

#2 casefold()
string_methods_dict.update(casefold = array_of_strings[1].casefold())

#3 center(position of the string on a line:int, "character" to occupy the spaces front and back of the text)
string_methods_dict.update(center = array_of_strings[2].center(20,"-"))

#4 count() counts the sub string
string_methods_dict.update(count = array_of_strings[3].count('RTE'))

#5 endwith()
string_methods_dict.update(endswith = array_of_strings[4].endswith(('r','t')))

#6 expandtabs()
string_methods_dict.update(expandtabs = array_of_strings[5].expandtabs(20))

#7 find()
string_methods_dict.update(find = array_of_strings[6].find('create'))

#8 format()
#usage method - 1 
string_methods_dict.update(format_M_1 = array_of_strings[7].format('class', 'Character'))
#usage method - 2
string_methods_dict.update(format_M_2 = array_of_strings[8].format(type="class", Character="jon snow"))

#9 format_map()
mapping_data:dict = {'class':"books", "instance":"Game of thrones"}
string_methods_dict.update(format_map = array_of_strings[9].format_map(mapping_data))

#10 index()
string_methods_dict.update(index = array_of_strings[9].index("done"))

#11 isalnum() is string alpha numeric [alphabets and numbers]
#usage method - 1 
string_methods_dict.update(isalnum_1 = array_of_strings[10].isalnum())
#usage method - 2
string_methods_dict.update(isalnum_2 = array_of_strings[11].isalnum())

#12 isalpha() [only alphabets]
string_methods_dict.update(isalpha = array_of_strings[11].isalpha())

#13 isascii() [only ASCCI]
string_methods_dict.update(isascii = array_of_strings[11].isascii())

#14 isdecimal() #if a string is decimal and numeric
string_methods_dict.update(isdecimal = array_of_strings[12].isdecimal())

#15 isidentifier()
#usage method - 1
string_methods_dict.update(isidentifier_1 = array_of_strings[12].isidentifier())
#usage method - 2
string_methods_dict.update(isidentifier_2 = array_of_strings[13].isidentifier())

#16 islower() checks the string is lower case
string_methods_dict.update(islower = array_of_strings[14].islower())

#17 isprintable() escape sequences such as \t ,\n, \r cannot be printed
#usage method - 1
string_methods_dict.update(isprintable_1 = array_of_strings[5].isprintable())
#usage method - 2
string_methods_dict.update(isprintable_2 = array_of_strings[13].isprintable())

#18 isspace()
string_methods_dict.update(isspace = array_of_strings[15].isspace())

#19 istitile()
#usage method - 1
string_methods_dict.update(istitle_1 = array_of_strings[16].istitle())
#usage method - 2
string_methods_dict.update(istitle_2 = array_of_strings[17].istitle())

#20 isupper()
string_methods_dict.update(isupper = array_of_strings[16].isupper())

#21 join() joins the elements on a list in to a string
string_methods_dict.update(join = array_of_strings[18].join(["join", "the", "text", "with", "underscore"]))

#22 ljust(include the text count :int, text to be tailed:str) appends the character at the end of the string
string_methods_dict.update(ljust = array_of_strings[19].ljust(15, "_"))

#23 lower() convert the text into lower
string_methods_dict.update(lower = array_of_strings[20].lower())

#24 lstrip(words to be removed from the string from left)
string_methods_dict.update(lstrip = array_of_strings[20].lstrip('UPPER_'))

#25 rstrip()
string_methods_dict.update(rstrip = array_of_strings[20].rstrip('_LOWER'))

#26 maketrans() and translate()
#usage method - 1
string_methods_dict.update(maketrans_1 = array_of_strings[21].maketrans('B', '@'))
var_str:str = array_of_strings[21].maketrans('B', '@')
string_methods_dict.update(translate_1 = array_of_strings[21].translate(var_str))
#usage method - 2
string_methods_dict.update(maketrans_2 = array_of_strings[21].maketrans(translate))
var_str:str = array_of_strings[21].maketrans(translate)
string_methods_dict.update(translate_2 = array_of_strings[21].translate(var_str))

#27 partition(provide the letter from where the partition shd be done: str)
string_methods_dict.update( partition = array_of_strings[22].partition('='))

#28 removesuffix("mention the suffix to be removed from the string":str)
string_methods_dict.update(removesuffix = array_of_strings[23].removesuffix('valid'))

#29 replace()
string_methods_dict.update(replace = array_of_strings[24].replace('wise', 'bold',1))

#30 rfind(input a text to be found in the string:str)
string_methods_dict.update(rfind_1 = array_of_strings[24].rfind('wise'))
string_methods_dict.update(rfind_2 = array_of_strings[24].rfind('good'))

#31 rindex()
string_methods_dict.update(rindex = array_of_strings[24].rindex('wise'))

#32 rjust()
string_methods_dict.update(rjust = array_of_strings[25].rjust(20,'-'))

#33 rpartition()
string_methods_dict.update(rpartition = array_of_strings[25].rpartition(' '))

#34 rsplit()/split
#maxsplit
string_methods_dict.update(rsplit_maxsplit = array_of_strings[24].rsplit(maxsplit=3))
#sep - seperator
string_methods_dict.update(rsplit_sep = array_of_strings[24].rsplit(sep=' '))

#35  swapcase()
string_methods_dict.update(swapcase = array_of_strings[25].swapcase())

#36 title()
string_methods_dict.update(title = array_of_strings[24].title())

#37 upper()
string_methods_dict.update(upper = array_of_strings[26].upper())

#38 zfill()
string_methods_dict.update(zfill = array_of_strings[27].zfill(10))

#printing the contents of the dictionary
for keys,value in string_methods_dict.items():
    print(f'key : "{keys}" -> value : "{value}"')