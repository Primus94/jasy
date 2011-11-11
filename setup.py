#!/usr/bin/env python3

import sys, os

major, minor = sys.version_info[:2]

if major < 3:
    raise Exception("Jasy requires Python 3")

# Use the best available install method
# The future will be distutils2 and will replace distutils/setuptools/distribute
# See also: http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-and-setuptools

# Load distutils and switch to distribute afterwards
from distutils.core import setup
from distribute_setup import use_setuptools
use_setuptools()

# Extend PYTHONPATH with local 'lib' folder
jasyroot = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]), os.pardir, "lib"))
sys.path.insert(0, jasyroot)

# Import Jasy for version info etc.
import jasy

setup(
      name = 'jasy',
      version = jasy.VERSION,
      
      author = 'Sebastian Werner',
      author_email = 'info@sebastian-werner.net',
      
      url = 'http://github.com/wpbasti/jasy',
      download_url = "http://pypi.python.org/packages/source/s/jasy/jasy-%s.tar.gz" % jasy.VERSION,
      
      license = "http://www.apache.org/licenses/LICENSE-2.0",
      
      description = "A build system for JavaScript focused web projects",
      long_description = open('readme.txt').read(),

      packages = [
        'jasy',
        'jasy.core',
        'jasy.ext',
        'jasy.optimizer',
        'jasy.parser',
        'jasy.process',
        'jasy.tokenizer'
      ],
      
      package_dir = {
        '': 'lib'
      },
      
      package_data = {
        'jasy': [
          'data/cldr/VERSION', 
          'data/cldr/keys/*.xml', 
          'data/cldr/main/*.xml', 
          'data/cldr/supplemental/*.xml'
        ]
      },
      
      scripts = [
        "bin/jasy", 
        "bin/jscompress", 
        "bin/jsdeps", 
        "bin/jsmeta", 
        "bin/jsoptimize", 
        "bin/jstree"
      ],
      
      data_files = [
        ("doc", [
          "license.txt"
        ])
      ]
)
