from linkedQFile import *


class Syntaxfel(Exception):
    pass


def readMolekyl(q):
    if q.peek() is None:
        return
    # läsa av atomen
    readAtom(q)
    # måste sluta med siffra eller ingenting
    val = q.peek()
    if val is None:
        pass
    elif val.isdigit():
        readNum(q)
    else:
        raise Syntaxfel("För många stora/små bokstäver vid radslutet " + molekyl)


def readAtom(q):
    # första bokstav stor
    letter = q.peek()
    if readUpperLetter(letter):
        q.dequeue()
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + q.get_rest())
    val = q.peek()
    # om andra bokstav liten, dequeue, oavsett gå vidare
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
    while not q.isEmpty() and q.peek().isdigit():
        num += q.dequeue()

    if q.peek() is not None:
        raise Syntaxfel("Atom avslutas inkorrekt")
    if num[0] == "0":
        raise Syntaxfel("För litet tal vid radslutet " + num[1:])
    if int(num) < 2:
        raise Syntaxfel("För litet tal vid radslutet")


def kollaMolekylen(formel):
    q = LinkedQ()
    q.mega_enqueue(formel)
    try:
        readMolekyl(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as e:
        return str(e)
