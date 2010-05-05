##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.hookable package

$Id$
"""

import os

from setuptools import setup, find_packages, Extension

setup(name='zope.hookable',
      version = '3.4.2dev',
      url='http://svn.zope.org/zope.hookable',
      license='ZPL 2.1',
      description='Zope hookable',
      author='Zope Foundation and Contributors',
      author_email='zope3-dev@zope.org',
      long_description="Hookable object support.",

      packages=find_packages('src'),
      package_dir = {'': 'src'},
      ext_modules=[Extension("zope.hookable._zope_hookable",
                             [os.path.join('src', 'zope', 'hookable',
                                           "_zope_hookable.c")
                              ]),
                   ],
      namespace_packages=['zope',],
      extras_require=dict(test=['zope.testing']),
      install_requires=['setuptools'],
      include_package_data = True,

      zip_safe = False,
      )
