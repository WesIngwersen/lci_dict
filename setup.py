from setuptools import setup

setup(
    name='lci_dict',
    version='0.1',
    packages=['lci_dict'],
    url='https://github.com/WesIngwersen/lci_dict',
    install_requires=[
        'pandas>=0.24',
        'olca-ipc>=0.0.6'
    ],
    license='CC0',
    author='Wesley Ingwersen',
    author_email='ingwersen.wesley@epa.gov',
    description=''
)
