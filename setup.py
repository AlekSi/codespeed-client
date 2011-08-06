#!/usr/bin/env python

from distutils.core import setup

setup(
    name='codespeed-client',
    version='0.3.0',
    author='Alexey Palazhchenko',
    author_email='alexey.palazhchenko@gmail.com',
    packages=['codespeed_client'],
    scripts=['scripts/codespeed-client'],
    url='https://github.com/AlekSi/codespeed-client',
    license='MIT',
    description='Library and command-line tool to push benchmark data to CodeSpeed.',
    long_description=open('README.rst').read(),
)
