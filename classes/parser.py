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
            self.remove_namespace(self.results, u'http://pdbml.pdb.org/schema/pdbx-v40.xsd')
            self.remove_namespace(self.results, u'http://pdbml.pdb.org/schema/pdbx-v42.xsd')
            self.remove_namespace(self.results, u'http://pdbml.pdb.org/schema/pdbx-v50.xsd')
        except:
            print("Invalid XML format file")
            exit()

        self.parse_atoms()
        self.parse_residues()

    def parse_atoms(self):
        for section in self.results:
            if section.tag != "atom_siteCategory": continue

            for obj in section:
                atom = PDBMLAtom(obj)
                self.atoms.append(atom)

    def parse_residues(self):
        # The list of parameters and searching
        attrs = self.residues_attributes()

        for section in self.results:
            if section.tag not in attrs: continue

            for obj in section:
                if obj.tag not in attrs: continue

                residue = PDBMLResidue(obj, self.atoms)
                self.residues.append(residue)

    # Statics and name of structure
    def get_name(self):
        if 'datablockName' in self.results.attrib:
            return self.results.attrib['datablockName']

        return ''

    def atoms_length(self):
        return str(len(self.atoms))

    def residues_length(self):
        return str(len(self.residues))

    def print_file_info(self):
        print("Protein: " + self.get_name())
        print("Atoms count: " + self.atoms_length())
        print("Residues count: " + self.residues_length())

    # Helper
    def remove_namespace(self, doc, namespace):
        ns = u'{%s}' % namespace
        nsl = len(ns)
        for elem in doc.getiterator():
            if elem.tag.startswith(ns):
                elem.tag = elem.tag[nsl:]

    def residues_attributes(self):
        return [
            'pdbx_struct_mod_residueCategory',
            'pdbx_struct_mod_residue',
            'struct_site_genCategory',
            'struct_site_gen'
        ]
