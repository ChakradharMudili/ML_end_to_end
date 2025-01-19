from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement = []
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirement]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements
    

setup(
    name = "ML End to End Project",
    version = '0.0.1',
    author = 'Devi Chakradhar Mudili',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)