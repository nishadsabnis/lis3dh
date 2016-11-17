# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='lis3dh',
    version='0.0.1',
    description='Python package for the LIS3DH accelerometer',
    long_description=readme,
    author='Nishad Sabnis',
    author_email='nishadsabnis@gmail.com',
    url='https://github.com/nishadsabnis/lis3dh',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
