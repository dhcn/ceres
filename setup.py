#!/usr/bin/env python

import os
from glob import glob
from distutils.core import setup


setup(
  name='ceres',
  version='0.10.0-rc1',
  url='http://graphiteapp.org/',
  author='Chris Davis',
  author_email='chrismd@gmail.com',
  license='Apache Software License 2.0',
  description='Distributable time-series database',
  py_modules=['ceres'],
  scripts=glob('bin/*'),
  data_files=[('plugins/maintenance', glob('plugins/maintenance/*.py'))]
)
