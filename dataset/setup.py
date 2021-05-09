from setuptools import setup, find_packages

requirements = ['pandas', 'numpy', 'sklearn', 'imblearn']
setup(
    name="dataset",
    version="1.0.0",
    description="Module to load and use training/test datasets",
    packages=find_packages(),
    install_requires=requirements
)
