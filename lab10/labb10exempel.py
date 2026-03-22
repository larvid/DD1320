from molgrafik import *


class Ruta:
    def __init__(self, atom="()", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


mol = Ruta(atom="C", num=1)
mol2 = Ruta(atom="Cl", num=2)
mol.next = mol2
mol.down = mol2
mg = Molgrafik()
mg.show(mol)
