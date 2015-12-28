from setuptools import setup, find_packages

with open('requirements.txt','r') as fp:
        requirements = [ x.strip() for x in fp ]

setup(
    name='horizon-loadtime',
    version='0.0.1',
    url='https://github.com/alokjani/python-horizonspeedtest',
    author='Alok Jani',
    author_email='Alok.Jani@ril.com',
    description='Measure Page Load Times for OpenStack Horizon',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'horizon-speedtest = horizonspeedtest.client:main',
            ]
        },
)
