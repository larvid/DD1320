from linkedQFile import *


class Syntaxfel(Exception):
    pass


def __init__(self, name):
    self.name = name


def readMolekyl(q):
    if q.peek() is None:
        return
    readAtom(q)
    val = q.peek()
    if val is not None and val.isdigit():
        readNum(q)


def readAtom(q):
    readUpperLetter(q)
    val = q.peek()
    if val is not None and val.islower():
        readLowerLetter(q)


def readUpperLetter(q):
    val = q.dequeue()
    u_alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    if val not in u_alfabet:
        rest = ""
        tmp = q.show()
        if tmp is not None:
            rest = "".join(tmp)
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + val + rest)


def readLowerLetter(q):
    val = q.dequeue()
    l_alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    if val not in l_alfabet:
        rest = ""
        tmp = q.show()
        if tmp is not None:
            rest = "".join(tmp)
        raise Syntaxfel("Ej liten bokstav " + val + rest)


def readNum(q, num=""):
    val = q.peek()

    if val is None or not val.isdigit():
        if num == "":
            return
        if int(num) <= 1:
            raise Syntaxfel("För litet tal vid radslutet ")
        return

    if val == "0" and num == "":
        q.dequeue()
        rest = "".join(q.show() or [])
        raise Syntaxfel("För litet tal vid radslutet " + rest)

    num += q.dequeue()
    return readNum(q, num)


def kollaMolekylen(formel):
    q = LinkedQ()
    q.mega_enqueue(formel)
    try:
        readMolekyl(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as e:
        return str(e)
