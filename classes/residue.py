# coding: utf8
class PDBMLResidue:
    def __init__(self, residue, atoms = []):
        self.residue = residue
        self.atoms = atoms

    # returns the residue name, e.g. "ASN"
    def get_resname(self):
        attrs = ['auth_comp_id', 'label_comp_id']

        for obj in self.residue:
            if obj.tag in attrs and len(obj.text) > 0:
                return obj.text

        return  ''

    # Full name
    def get_details(self):
        for obj in self.residue:
            if obj.tag == 'details' and len(obj.text) > 0: return obj.text

        return  ''

    # returns the SEGID, e.g. "CHN1"
    def get_segid(self):
        attrs = ['auth_seq_id', 'label_seq_id']

        for obj in self.residue:
            if obj.tag in attrs and len(obj.text) > 0:
                return obj.text

        return  ''

    # test if a residue has a certain atom
    def has_atom(self, name):
        for atom in self.atoms:
            if atom.get_name() == name and atom.get_comp_id() == self.get_resname():
                return True

        return False

    def print_data(self):
        print("Residue: " + self.get_resname())
        print("Details: " + self.get_details())
        print("Seq ID: " + self.get_segid())
        print("Has 'P' atom: " + str(self.has_atom('P')))
        print("Has 'NOPE' atom: " + str(self.has_atom('NOPE')))
        print("----")
