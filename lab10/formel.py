from linkedQFile import *
from atomvikter import atomvikt
from molgrafik import *


class Syntaxfel(Exception):
    pass


def readFormel(q):
    mol, vikt = readMol(q)
    if q.peek() is not None:
        if q.peek() == ")":
            raise Syntaxfel("Felaktig gruppstart vid radslutet " + q.get_rest())
        else:
            raise Syntaxfel("Något gick snett :/")

    return mol, vikt


def readMol(q):
    if q.peek() is None or q.peek() == ")":
        return None, 0
    ruta, group_vikt = readGroup(q)
    next, mol_vikt = readMol(q)
    ruta.next = next

    return ruta, group_vikt + mol_vikt


def readGroup(q):
    val = q.peek()
    if val == "(":
        q.dequeue()
        down, mol_vikt = readMol(q)
        if q.peek() != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet")
        q.dequeue()
        if q.peek() is None:
            raise Syntaxfel("Saknad siffra vid radslutet " + q.get_rest())
        if not q.peek().isdigit():
            raise Syntaxfel("Saknad siffra vid radslutet " + q.get_rest())
        num = readNum(q)
        ruta = Ruta(num=num)
        ruta.down = down
        vikt = mol_vikt * num
    else:
        if not readUpperLetter(val) and not readLowerLetter(val):
            raise Syntaxfel("Felaktig gruppstart vid radslutet " + q.get_rest())
        atom, atomvikt = readAtom(q)
        num = readNum(q)
        ruta = Ruta(atom=atom, num=num)
        vikt = atomvikt * num

    return ruta, vikt


def readAtom(q):
    val1 = q.peek()
    if readUpperLetter(val1):
        q.dequeue()
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + q.get_rest())

    val2 = q.peek()
    if readLowerLetter(val2):
        q.dequeue()
    else:
        val2 = ""
    atom = val1 + val2
    if atom in atomvikt:
        return atom, atomvikt[atom]
    else:
        raise Syntaxfel("Okänd atom vid radslutet " + q.get_rest())


def readUpperLetter(letter):
    u_alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    if letter is None:
        return False
    if letter in u_alfabet:
        return True
    else:
        return False


def readLowerLetter(letter):
    l_alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    if letter is None:
        return False
    if letter in l_alfabet:
        return True
    else:
        return False


def readNum(q, num=""):
    digit = q.peek()
    if digit is None:
        return 1
    if not digit.isdigit():
        return 1
    if digit == "0":
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet " + q.get_rest())

    while not q.isEmpty() and q.peek().isdigit():
        num += q.dequeue()

    if int(num) < 2:
        raise Syntaxfel("För litet tal vid radslutet " + q.get_rest())

    return int(num)


def kollaFormeln(formel):
    q = LinkedQ()
    q.mega_enqueue(formel)
    try:
        readFormel(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as e:
        return str(e)


def weight(mol):
    if mol is None:
        return 0

    if mol.atom == "()":
        mol_vikt = weight(mol.down)
        vikt1 = mol_vikt * mol.num
    else:
        at_vikt = atomvikt[mol.atom]
        vikt1 = at_vikt * mol.num

    vikt2 = weight(mol.next)
    vikt = vikt1 + vikt2
    return vikt
