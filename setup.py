# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

setup(
    name='mcp23017',
    version='0.1.0',
    description='MCP23017 Library',
    long_description=open("README.md", 'r').read(),
    long_description_content_type='text/markdown',
    author='Mirko Haeberlin',
    author_email='mirko.haeberlin@sensorberg.com',
    url='https://github.com/sensorberg-dev/MCP23017-python',
    packages=find_packages(exclude=('tests', 'docs'))
)
