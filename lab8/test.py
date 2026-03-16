import unittest
from molekyl import *


class MolekylTest(unittest.TestCase):

    def test_korrekt(self):
        self.assertEqual(kollaMolekylen("He"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(kollaMolekylen("He2"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(kollaMolekylen("He105"), "Formeln är syntaktiskt korrekt")

    def test_fel(self):
        self.assertEqual(kollaMolekylen("He1"), "För litet tal vid radslutet ")
        self.assertEqual(kollaMolekylen("He02"), "För litet tal vid radslutet 2")
        self.assertEqual(kollaMolekylen("H0"), "För litet tal vid radslutet ")
        self.assertEqual(kollaMolekylen("8"), "Saknad stor bokstav vid radslutet 8")
        self.assertEqual(
            kollaMolekylen("cr12"), "Saknad stor bokstav vid radslutet cr12"
        )


if __name__ == "__main__":
    unittest.main()
