try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = ""
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='posterierr',
    version='0.1',
    author='Johannes Buchner',
    author_email='buchner.johannes@gmx.at',
    packages=['posterierr'],
    url='https://github.com/JohannesBuchner/posterierr',
    license='LICENSE',
    description='MCMC Posterior Sample Error Propagation',
    long_description=long_description,
    install_requires=[
        "scipy",
        "numpy",
    ],
)

