from linkedQFile import *
from periodic_elements import *


class Syntaxfel(Exception):
    pass


def readFormel(q):
    readMol(q)
    if q.peek() is not None:
        if q.peek() == ")":
            raise Syntaxfel("Saknad vänsterparentes vid radslutet")
        else:
            raise Syntaxfel("Något gick snett :/")


def readMol(q):
    if q.peek() is None or q.peek() == ")":
        return
    readGroup(q)
    readMol(q)


def readGroup(q):
    val = q.peek()
    if val == "(":
        q.dequeue()
        readMol(q)
        if q.peek() != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet")
        q.dequeue()
        if q.peek() is None:
            raise Syntaxfel("Saknad siffra vid radslutet" + q.get_rest())
        if not q.peek().isdigit():
            raise Syntaxfel("Saknad siffra vid radslutet" + q.get_rest())
        readNum(q)
    else:
        readAtom(q)
        readNum(q)


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
    if not atom in periodic_elements:
        raise Syntaxfel("Atom finns inte vid radslutet " + q.get_rest())


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
        return None
    if not digit.isdigit():
        return None
    if digit == "0":
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet " + q.get_rest())

    while not q.isEmpty() and q.peek().isdigit():
        num += q.dequeue()

    if int(num) < 2:
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet " + q.get_rest())
