import unittest
from classes.parser import PDBMLParser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = PDBMLParser('test/ok.xml')
        self.parser.load()
        pass

    # Case 1: The file does not exist
    def test_file_does_not_exist(self):
        no_file = PDBMLParser('xml/nofile.xml')

        with self.assertRaises(SystemExit):
            no_file.load()

    # Case 2: Incorrect structure of the file
    def test_file_is_corrupted(self):
        corrupted = PDBMLParser('test/corrupted.xml')

        with self.assertRaises(SystemExit):
            corrupted.load()

    # Case 3: Lists of atoms and resiues (with 1 element)
    def test_atoms_and_residues_count(self):
        self.assertEqual(len(self.parser.residues), 1)
        self.assertEqual(len(self.parser.atoms), 1)

    # Case 4: Residue data matches
    def test_pass_residue(self):
        self.assertEqual(self.parser.residues[0].get_resname(),'2MG')
        self.assertEqual(self.parser.residues[0].has_atom('OP3'), False)

    # Case 5: The structure contains an atom
    def test_pass_atom(self):
        self.assertEqual(self.parser.atoms[0].get_name(),'OP3')
        self.assertEqual(self.parser.atoms[0].get_bfactor(), 99.85)

if __name__ == '__main__':
    unittest.main()
