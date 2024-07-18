from setuptools import find_packages,setup
# it will find all the available packages in the entire ml app

# for example there is a file __init__.py inside src folder.
# our find_packages will find it as a package and install it on the initiation of our setup.py

from typing import List

HYPHEN_E_DOT = '-e .'

# get_requirements will return a list of string 
def get_requirements(file_path : str) -> List[str]:
    '''this function will return a list of requirement saved in requirements.txt'''

    requirement = []
    with open(file_path) as file_obj:
        '''we are opening file by open method as temporary file_obj and readlines will read all the file line by line and whenever we will be reading line by line there will be ('n') added after end of each line and we need to replace it by looping or other method'''

        requirements = file_obj.readlines()
        requirements = [req.replace("\n" , "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
    
            




# setup has all the brief information about our model
setup(
name = 'mlproject',
version = '0.0.1',
author = 'sushant',
author_email = 'rsushant441@gmail.com',
packages = find_packages(),
# install_requires = ['pandas','numpy','etc'] 

# we will create get_requirements function so to fetch all the requirement list
install_requires = get_requirements('requirements.txt')




)