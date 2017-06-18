# coding: utf8

from pathlib import Path
from .atom import PDBMLAtom
from .residue import PDBMLResidue

import xml.etree.ElementTree as etree

class PDBMLParser:
    results = None
    atoms = []
    residues = []

    def __init__(self, file_path):
        self.file_path = file_path
        self.ns = "{http://pdbml.pdb.org/schema/pdbx-v40.xsd}"

    def load(self):
        xml_file = Path(self.file_path)

        if xml_file.is_file():
            return self.parse_xml()

        print("Path to the file is incorrect or the file does not exist.")
        exit()

    def parse_xml(self):
        try:
            tree = etree.parse(self.file_path)
            self.results = tree.getroot()
        except:
            print("Invalid XML format file")
            exit()

        self.parse_atoms()
        self.parse_residues()

    def parse_atoms(self):
        for section in self.results:
            if section.tag == self.ns + "atom_siteCategory":
                for obj in section:
                    atom = PDBMLAtom(self.ns, obj)
                    self.atoms.append(atom)

    def parse_residues(self):
        for section in self.results:
            if section.tag == self.ns + "pdbx_struct_mod_residueCategory":
                for obj in section:
                    residue = PDBMLResidue(self.ns, obj, self.atoms)
                    self.residues.append(residue)

    def get_name(self):
        if 'datablockName' in self.results.attrib:
            return self.results.attrib['datablockName']

        return ''

    def atoms_length(self):
        return str(len(self.atoms))

    def residues_length(self):
        return str(len(self.residues))

    def print_file_info(self):
        print("Structure: " + self.get_name())
        print("Atoms count: " + self.atoms_length())
        print("Residues count: " + self.residues_length())
