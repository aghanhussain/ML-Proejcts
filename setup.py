from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''This function return the list of requirements'''
    requirements = []
    with open(file_path,'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements



setup(
 name='mlproject',
 version='0.0.1',
 author = 'NasirHussain',
 author_email = 'aghanhussain@gmail.com',
 packages=find_packages(),
#  install_requires = ['pandas','numpy','seaborn','matplotlib.pyplot']
install_requires = get_requirements('requirements.txt')
)