from setuptools import find_packages
from distutils.core import setup
import os

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
	# Name of the package 
	name='Agreement',
	# Packages to include into the distribution 
	packages=find_packages('.'),
	# Start with a small number and increase it with 
	# every change you make https://semver.org 
	version='1.0',
	# Chose a license from here: https: // 
	# help.github.com / articles / licensing - a - 
	# repository. For example: MIT
	license='MIT',
	# Short description of your library 
	description='Agreement is a very simple module that prints on screen with colors the rules, agreed by convention, of python.',
	# Long description of your library 
	long_description=long_description,
	long_description_content_type='text/markdown',
	# Your name 
	author='VidalGB',
	# Your email 
	author_email='vidalgb.cantacto@gmail.com',
	# Either the link to your github or to your website 
	url='https://github.com/VidalGB/',
	# Link from which the project can be downloaded 
	download_url='https://github.com/VidalGB/Agreement/releases/tag/v1.0',
	# List of keywords 
	keywords=['Agreement','Python','Sintax','Convantion','Rules','Tutorial'],
	# List of packages to install with this one 
	install_requires=[],
	# https://pypi.org/classifiers/ 
	classifiers=[],
	# Python version
	python_requires='>=3'
)
