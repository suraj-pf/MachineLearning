from setuptools import setup, find_packages 
from typing import List

HYPEN_E_DOT = '-e .'    

def get_requirements(file_path: str) -> list:
    '''Read the requirements from a file and return as a list. '''

    requirements = []

    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name='my_package',
    version='0.1.0',
    author='Your Name', 
    author_email='',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)