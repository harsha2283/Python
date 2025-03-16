Source to setup a virtual environment in the python is as follows  

+------------------------------------------------------+
       https://www.youtube.com/watch?v=KxvKCSwlUv8
+------------------------------------------------------+

path/python.exe -m venv venv_name

venv_name = name of your venv u wanted for your projects 


To activate the venv 
----------------------
venv_name\script\activate.bat 

To install the set of packages or library versions used for your projects you can list all the packages or if u need the specific version of the package you mention that as well
|_example_:-
pandas==1.8.2

1 - it's the Major version of the package
8 - Minor version of the package
2 - Patch version of the package

run the following command in your created venv to install those packages
--------------------------------
pip install -r path\packages_with_versions.txt 

