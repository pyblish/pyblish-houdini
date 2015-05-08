#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This setup script packages pyblish-houdini"""

from setuptools import setup, find_packages

import os
import imp

version_file = os.path.abspath('pyblish_houdini/version.py')
version_mod = imp.load_source('version', version_file)
version = version_mod.version


def get_readme():
    with open('README.txt') as f:
        readme = f.read()
    return readme


classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
]


setup(
    name='pyblish-houdini',
    version=version,
    packages=find_packages(),
    url='https://github.com/pyblish/pyblish-houdini',
    license='LGPL',
    author='Abstract Factory and Contributors',
    author_email='marcus@abstractfactory.io',
    description='Houdini integration of Pyblish',
    long_description=get_readme(),
    zip_safe=False,
    classifiers=classifiers,
    package_data={
        'pyblish_houdini': ['plugins/*.py',
                            'houdini_path/*.py',
                            'houdini_path/scripts/*.py']
    },
    install_requires=["pyblish>=1.0.12",
                      "pyblish-endpoint>=1.1.0",
                      "pyblish-qml>=0.2.0"]
)
