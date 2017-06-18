#!/usr/bin/env python
# coding: utf8

#  Before the launching in the project catalog:
#   pip install -r requirements.txt

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import sys

from classes.logger import PDBMLLogger
from classes.parser import PDBMLParser

file_path = input("Path to the file (e.g. xml/test.xml): ")
print('\n\n')

# Parser start and creation of the output file
parser = PDBMLParser(file_path)
sys.stdout = PDBMLLogger('output.txt')

parser.load()
parser.print_file_info()

print('\n\n')

# Test display of the selected atoms
for index, item in enumerate(parser.atoms):
    if index == 8: break
    item.print_data()

# By analogy for the residues:
for index, item in enumerate(parser.residues):
    if index == 8: break
    item.print_data()
