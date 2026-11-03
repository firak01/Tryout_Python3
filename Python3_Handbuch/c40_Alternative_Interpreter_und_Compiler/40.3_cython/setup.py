#!/usr/bin/env python

from setuptools import setup
from Cython.Build import cythonize


setup(
    ext_modules = cythonize("beispiel_02_sortieren_cython.pyx")
)
setup(
    ext_modules = cythonize("beispiel_03_sortieren_cython_2.pyx")
)
setup(
    ext_modules = cythonize("beispiel_04_sortieren_cython_3.pyx")
)
setup(
    ext_modules = cythonize("beispiel_05_sortieren_cython_4.pyx")
)
