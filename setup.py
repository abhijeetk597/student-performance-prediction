from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str)->List[str]:
    """
    This function will return the list of requirements.

    Args:
        file_path: path of requirements.txt file
    Returns:
        list of requirements
    """
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="studentperformanceprediction",
    version="0.0.1",
    author="Abhijeet",
    author_email="abhijeetk597.ds@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)