from setuptools import setup

# Useful for hosting on pypy if we want the project as a package
with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Atharva Nagbhidkar'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email ='atharva.n.2309@gmail.com',
    description = 'A simple package for game recommendation.',
    long_description = 'tetx/markdown',
    package = [SRC_REPO],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS,
 )
