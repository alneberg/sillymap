from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(name='sillymap',
        version='0.2.0',
        description='A silly implementation of a short read mapper for the course DD3436.',
        url='http://github.com/alneberg/sillymap',
        author='Johannes Alneberg',
        author_email='alneberg@kth.se',
        license='MIT',
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
        zip_safe=False,
        scripts=['bin/sillymap'],
        ext_modules = cythonize(["sillymap/burrows_wheeler.pyx", "sillymap/rank_lookup.pyx", "sillymap/count_lookup.pyx", "sillymap/backwards_search.pyx", "sillymap/index.pyx", "sillymap/mapper.pyx"])
   )
