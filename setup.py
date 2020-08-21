#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='odc-ee',
      version='0.0.2',
      description='EE Indexing Tools',
      author='Andrew Lubawy',
      author_email='andrew.m.lubawy@ama-inc.com',
      install_requires=[
          "PyYAML>=5.3.1",
          "click-plugins>=1.1.1",
          "click>=7.1.2",
          "google-api-core>=1.17.0",
          "google-api-python-client>=1.8.3",
          "google-auth-httplib2>=0.0.3",
          "google-auth>=1.15.0",
          "googleapis-common-protos>=1.51.0",
          "numpy>=1.18.4",
          "pandas>=1.0.3",
          "pyproj>=2.6.1",
          "tqdm>=4.46.0",
          ],
      packages=find_packages(),
      scripts=['scripts/index_ee', 'scripts/new_product'],)
