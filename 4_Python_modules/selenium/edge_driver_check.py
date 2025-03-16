import os

if os.path.exists("msedgedriver.exe"):
    print("msedgedriver.exe found in the current directory.")
else:
    print("msedgedriver.exe not found in the current directory.")