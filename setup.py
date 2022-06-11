# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md", 'r') as file:
    long_description = file.read()

with open("requirements.txt", 'r') as file:
    dependencies = list(map(lambda x: x.strip(), file.readlines()))

setup(
   name='Weather-ip',
   version='0.1',
   description='Module for getting weather by ip',
   license="MIT",
   long_description=long_description,
   author='Tarkhanov Michael',
   author_email='tarmd@ya.com',
   install_requires=dependencies
)