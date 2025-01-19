# setup.py

from setuptools import setup, find_packages

setup(
    name='age_printer',
    version='0.1',
    packages=find_packages(),
    description='A simple package to print user age.',
    author='Sara',
    author_email='sarabr082@gmail.com',
    url='https://github.com/sarabarati/age_printer',  # Update with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
