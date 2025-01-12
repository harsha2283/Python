# Python code​​​​​​‌‌​​​‌​‌‌‌‌‌‌​​​​​​‌​​​​​ below
# Use print("messages...") to debug your solution.

special_char = ["!","?","'","."," ",","]
def is_palindrome(teststr):
    teststr = map(lambda teststr:teststr.lower(), teststr)
    # Your code goes here.
    data = ''.join(filter(str.isalnum, teststr))
    str_list = list(data)
    if str_list == str_list[::-1]:
        return True
    else:
        return False

test_words = ["Hello World!","Radar!","Mama?","Madam, I'm Adam.",
    "Race car!"]
for pal in test_words:
    if is_palindrome(pal):
        print(f"The string {pal} is a palindrome")
    else:
        print(f"The string {pal} is not a palindrome")