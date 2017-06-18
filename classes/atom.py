# coding: utf8
from .vector import Vector

class PDBMLAtom:
    atom = None

    def __init__(self, atom):
        self.atom = atom

    # atom name (spaces stripped, e.g. "CA")
    def get_name(self):
        return self.get_id()

    # id (equals atom name)
    def get_id(self):
        attrs = ['auth_atom_id', 'label_atom_id']

        for obj in self.atom:
            if obj.tag in attrs and len(obj.text) > 0:
                return obj.text

        return ''

    # atomic coordinates - [x,y,z] array
    def get_coord(self):
        cords = []
        attrs = ['Cartn_x', 'Cartn_y', 'Cartn_z']

        for obj in self.atom:
            if obj.tag in attrs: cords.append(float(obj.text))

        return cords

    # atomic coordinates as Vector object
    # Vector class: https://gist.github.com/mcleonard/5351452
    def get_vector(self):
        v = self.get_coord()
        if len(v) < 1: return Vector(0,0)
        return Vector(v[0], v[1], v[2])

    # isotropic B factor
    def get_bfactor(self):
        for obj in self.atom:
            if obj.tag == 'B_iso_or_equiv': return float(obj.text)

    # occupancy
    def get_occupancy(self):
        for obj in self.atom:
            if obj.tag == 'occupancy': return float(obj.text)

    # alternative location specifier
    def get_altloc(self):
        for obj in self.atom:
            if obj.tag == 'label_alt_id': return obj.text

        return ''

    # atom name (with spaces, e.g. ".CA.")
    def get_fullname(self):
        return "." + self.get_name() +  "."

    # residue
    def get_comp_id(self):
        attrs = ['auth_comp_id', 'label_comp_id']

        for obj in self.atom:
            if obj.tag in attrs and len(obj.text) > 0:
                return obj.text

        return ''

    # Display information
    def print_data(self):
        print("Atom ID: " + self.get_name())
        print("Full name: " + self.get_name())
        print("Coordinates (X,Y,Z array): " + str(self.get_coord()))
        print("Vector (normalized): " + str(self.get_vector().norm()))
        print("B Factor: " + str(self.get_bfactor()))
        print("Occupancy: " + str(self.get_occupancy()))
        print("Alt Loc: " + str(self.get_altloc()))
        print("Residue name: " + self.get_comp_id())
        print("----")
