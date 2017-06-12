class PDBMLResidue:
    def __init__(self, namespace, residue, atoms):
        self.residue = residue
        self.atoms = atoms
        self.ns = namespace

    # returns the residue name, e.g. "ASN"
    def get_resname(self):
        attrs = [self.ns + 'auth_comp_id', self.ns + 'label_comp_id']

        for obj in self.residue:
            if obj.tag in attrs and len(obj.text) > 0:
                return obj.text

        return  ''

    # Full name
    def get_details(self):
        for obj in self.residue:
            if obj.tag == self.ns + 'details' and len(obj.text) > 0: return obj.text

        return  ''

    # returns the SEGID, e.g. "CHN1"
    def get_segid(self):
        attrs = [self.ns + 'auth_seq_id', self.ns + 'labelseq_id']

        for obj in self.residue:
            if obj.tag in attrs and len(obj.text) > 0:
                return obj.text

        return  ''

    # test if a residue has a certain atom
    def has_id(self, name):
        for atom in self.atoms:
            if atom.get_name() == name and atom.get_comp_id() == self.get_resname():
                return True

        return False
