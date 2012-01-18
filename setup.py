#!/usr/bin/env python

from distutils.core import setup

setup(
    name='codespeed-client',
    version='0.3.3',
    author='Alexey Palazhchenko',
    author_email='alexey.palazhchenko@gmail.com',
    packages=['codespeed_client'],
    scripts=['scripts/codespeed-client'],
    url='https://github.com/AlekSi/codespeed-client',
    license='MIT',
    description='Library and command-line tool to push benchmark data to CodeSpeed.',
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Benchmark"]
)
