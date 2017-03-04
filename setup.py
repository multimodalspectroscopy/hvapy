from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    name='HVApy',
    version=0.1,
    description='Simple random number generators',
    author='Markus Dablander, Joshua Russell-Buckland',
    author_email='markus.dablander.16@ucl.ac.uk, \
    joshua.russell-buckland.15@ucl.ac.uk',
    url='http://github.com/multimodalspectroscopy/hvapy',
    license='MIT',
    ext_modules=cythonize("hva.pyx"),
    include_dirs=[numpy.get_include()]
)
