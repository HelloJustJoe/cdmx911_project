from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='cdmx911',
      version="0.1",
      description="CDMX911 Model Call Prioritization (api_pred)",
      license="WICHO",
      author="Alexa, Joe, Wicho",
      author_email="estebancoder@gmail.com",
      install_requires=requirements,
      packages=find_packages(),
      # test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
