#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.parser import PDBMLParser

file_path = input("Wprowadź ścieżkę do pliku z nazwą (może być relatywna do skryptu, np. xml/test.xml): ")
parser = PDBMLParser(file_path)

#parser = PDBMLParser("xml/test.xml")
parser.load()

print("Atoms count: " + parser.atoms_length())
print("Residues count: " + parser.residues_length())

# Testowe wyswietlanie kilku atomów:
for index, item in enumerate(parser.atoms):
    if index == 5: break

    print("Atom ID: " + item.get_name())
    print("Full name: " + item.get_name())
    print("Coordinates (X,Y,Z array): " + str(item.get_coord()))
    print("Vector (normalized): " + str(item.get_vector().norm()))
    print("B Factor: " + str(item.get_bfactor()))
    print("Occupancy: " + str(item.get_occupancy()))
    print("Alt Loc: " + str(item.get_altloc()))
    print("----")

# Analogicznie dla residues:
for index, item in enumerate(parser.residues):
    if index == 5: break

    print("Residue: " + item.get_resname())
    print("Details: " + item.get_details())
    print("Seq ID: " + item.get_segid())
    print("Has 'P' atom: " + str(item.has_id('P')))
    print("Has 'NOPE' atom: " + str(item.has_id('NOPE')))
    print("----")
