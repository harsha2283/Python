# using list comprehensions and creating a dictionary of ASCII characters and there respective decimal values

'''Keys = ASCII
Values = decimal'''
ascii_nd_hex = {key:value for key,value in zip(range(0,128),range(0,128))}

print(f"ASCII - Decimal ")
                
for keys,values in ascii_nd_hex.items():
    print(f"{chr(keys)}     -  {values}")