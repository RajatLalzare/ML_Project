from setuptools import find_packages,setup 
from typing import List 

hypen = '-e .' 
#v = 'n'

def get_requirements(file_path:str) -> List[str] :
    '''
    this function will return the list of the requirements

    ''' 

    requirements= []
    with open(file_path) as file_obj:

        requirements = file_obj.readline()
        requirements = [req.replace('\n','') for req in requirements]
        
        if hypen in requirements:
            requirements.remove(hypen) 
        #if v in requirements:
           # requirements.remove(v)
    return requirements

setup(
    name = 'ML_Projects',
    version='0.0.1',
    author='Dhotar Chor',
    author_email='rajatlalzare@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt') 


)