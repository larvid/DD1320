from linkedQFile import *


class Syntaxfel(Exception):
    pass


def readFormel(q):
    readMol(q)
    if q.peek() is not None:
        raise Syntaxfel("skräp")


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
        readNum(q)
    else:
        readAtom(q)
        readNum(q)


def readAtom(q):
    letter = q.peek()
    if readUpperLetter(letter):
        q.dequeue()
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + q.get_rest())

    val = q.peek()
    if readLowerLetter(val):
        q.dequeue()


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
    if not q.peek().isdigit():
        return None

    while not q.isEmpty() and q.peek().isdigit():
        num += q.dequeue()

    if num[0] == "0":
        raise Syntaxfel("För litet tal vid radslutet " + num[1:])
    if int(num) < 2:
        raise Syntaxfel("För litet tal vid radslutet")
