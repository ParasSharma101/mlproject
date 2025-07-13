from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str)-> List[str]:
    '''
    this function will return the list of requiements
    '''
    requiremets = []
    with open(file_path) as file_obj:
        requiements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requiements]


        if '-e .' in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Paras',
    author_email='parassharmaprof@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')


)