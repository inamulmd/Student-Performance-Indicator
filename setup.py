from setuptools import find_packages,setup
from typing import List


HPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
     '''
     this function will return the list of requirements
     '''
     requirements=[]
     with open(file_path) as file_obj:
        reuirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HPEN_E_DOT in requirements:
            requirements.remove(HPEN_E_DOT)

     return requirements        


setup(
    name="student_performance_indictor",
    version='0.0.1',
    author="Inamul",
    author_email='mdinamulh04@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)