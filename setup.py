from setuptools import setup, find_packages

setup(
    name='mcp23017',
    version='1.0.0',
    description='MCP23017 Library',
    long_description=open("README.md", 'r').read(),
    long_description_content_type='text/markdown',
    author='Mirko Haeberlin',
    author_email='mirko.haeberlin@open-things.de',
    url='https://github.com/open-thngs/MCP23017-python',
    packages=find_packages(exclude=('test', 'docs')),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
