from linkedQFile import *


class Syntaxfel(Exception):
    pass


def readMolekyl(q, molekyl):
    if q.peek() is None:
        return
    # läsa av atomen
    readAtom(q, molekyl)
    # måste sluta med siffra eller ingenting
    val = q.peek()
    if val is not None and val.isdigit():
        readNum(q)


def readAtom(q, molekyl):
    # första bokstav stor
    letter = q.dequeue()
    if not readUpperLetter(letter):
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + molekyl)
    val = q.peek()
    # om andra bokstav liten, dequeue, oavsett gå vidare
    if readLowerLetter(val):
        q.dequeue()


def readUpperLetter(letter):
    u_alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    if letter in u_alfabet:
        return True
    else:
        return False


def readLowerLetter(letter):
    l_alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    if letter in l_alfabet:
        return True
    else:
        return False


def readNum(q, num=""):
    while not q.isEmpty() and q.peek().isdigit():
        num += q.dequeue()
    if num[0] == "0":
        raise Syntaxfel("För litet tal vid radslutet " + num)
    if int(num) < 2:
        raise Syntaxfel("För litet tal vid radslutet " + num)


def kollaMolekylen(formel):
    q = LinkedQ()
    q.mega_enqueue(formel)
    try:
        readMolekyl(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as e:
        return str(e)
