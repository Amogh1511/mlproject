from setuptools import find_packages,setup
from typing import List

hypen = "-e ."
def get_requirements(file_path:str)->List[str]:
    "This function return the list of packages"
    packages=[]
    with open(file_path) as file:
        packages = file.readlines()
        packages = [pack.replace("/n","") for pack in packages]

        if hypen in packages:
            packages.remove(hypen)
    return packages
setup(
    name="mlproject",
    version="0.0.1",
    author= "Amogh",
    author_email="amoghmath2000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("packages.txt")


)