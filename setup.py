from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
    requirements = [req.replace('\n', '') for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements
    
setup(
    name='my_package',
    version='0.0.1',
    author='Sahil Gite',
    author_email='sahilgite01@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
# This setup script is used to package the Python project 'my_package'.
# It specifies the package name, version, author details, and required dependencies.
# The 'find_packages()' function automatically discovers all packages and subpackages.
# The 'install_requires' list includes the necessary libraries for the package to function correctly.
# This setup script is essential for distributing the package and managing its dependencies.