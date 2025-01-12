
#--------------------------------------------------------------------------------------#
#                           concept was learnt from                                    #
#             https://www.geeksforgeeks.org/python-list-slicing/
#                                                                                      #
#--------------------------------------------------------------------------------------#

#list_name[start : end : step]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Elements from index 0 to 2
a = list[:3]
print(a)

# Elements from index 3 to end
b = list[3:]
print(b)

# Get all Elements in the list 
c = list[::]
d = list[:]
print(c,"\n",d)

# Get all the Elements between the 2 indexes 
e = list[2:6]
print(e)

# Get elements with specific intervals 
f = list[::1]
g = list[::2]
h = list[1:8:3]
print(f,"\n",g,"\n",h)