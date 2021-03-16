# -*- coding: utf-8 -*-

# Learn more: https://github.com/yhu-insight/python-toolkit/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Python Toolkit',
    version='0.1.0',
    description='Python Toolkit Tutorials',
    long_description=readme,
    author='YuCheng Hu',
    author_email='yucheng.hu@insight.com',
    url='https://github.com/yhu-insight/python-toolkit',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

