#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Mon 16 Apr 08:18:08 2012 CEST

bob_packages = ['bob.core', 'bob.io.base']

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires=['bob.blitz'] + bob_packages))
from bob.blitz.extension import Extension, Library, build_ext

packages = ['boost']
boost_modules = ['system']

version = '2.0.0a0'

setup(

    name='bob.learn.activation',
    version=version,
    description='Bindings for bob.machine\'s Activation functors',
    url='http://github.com/bioidiap/bob.learn.activation',
    license='BSD',
    author='Andre Anjos',
    author_email='andre.anjos@idiap.ch',

    long_description=open('README.rst').read(),

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
      'setuptools',
      'bob.blitz',
      'bob.core',
      'bob.io.base',
    ],

    namespace_packages=[
      "bob",
      "bob.learn",
    ],

    ext_modules = [
      Extension("bob.learn.activation.version",
        [
          "bob/learn/activation/version.cpp",
        ],
        bob_packages = bob_packages,
        version = version,
        packages = packages,
        boost_modules = boost_modules,
      ),

      Library("bob.learn.activation.bob_learn_activation",
        [
          "bob/learn/activation/cpp/ActivationRegistry.cpp",
        ],
        bob_packages = bob_packages,
        version = version,
        packages = packages,
        boost_modules = boost_modules,
      ),

      Extension("bob.learn.activation._library",
        [
          "bob/learn/activation/activation.cpp",
          "bob/learn/activation/identity.cpp",
          "bob/learn/activation/linear.cpp",
          "bob/learn/activation/logistic.cpp",
          "bob/learn/activation/tanh.cpp",
          "bob/learn/activation/mult_tanh.cpp",
          "bob/learn/activation/main.cpp",
        ],
        bob_packages = bob_packages,
        version = version,
        packages = packages,
        boost_modules = boost_modules,
      ),
    ],

    cmdclass = {
      'build_ext': build_ext
    },

    classifiers = [
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],

  )
