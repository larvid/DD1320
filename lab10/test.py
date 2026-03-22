import unittest
from formel import kollaFormeln


class TestFormel(unittest.TestCase):

    def test_correct_formulas(self):
        """Testar formler som förväntas vara korrekta."""
        valid_cases = ["Na", "H2O", "Si(C3(COOH)2)4(H2O)7", "Na332"]
        for formel in valid_cases:
            with self.subTest(formel=formel):
                resultat = kollaFormeln(formel)
                self.assertEqual(resultat, "Formeln är syntaktiskt korrekt")

    def test_incorrect_formulas(self):
        """Testar formler som förväntas ge specifika felmeddelanden."""
        invalid_cases = [
            ("C(Xx4)5", "Okänd atom vid radslutet 4)5"),
            ("C(OH4)C", "Saknad siffra vid radslutet C"),
            ("C(OH4C", "Saknad högerparentes vid radslutet"),
            ("H2O)Fe", "Felaktig gruppstart vid radslutet )Fe"),
            ("H0", "För litet tal vid radslutet "),
            ("H1C", "För litet tal vid radslutet C"),
            ("H02C", "För litet tal vid radslutet 2C"),
            ("Nacl", "Saknad stor bokstav vid radslutet cl"),
            ("a", "Saknad stor bokstav vid radslutet a"),
            ("(Cl)2)3", "Felaktig gruppstart vid radslutet )3"),
            (")", "Felaktig gruppstart vid radslutet )"),
            ("2", "Felaktig gruppstart vid radslutet 2"),
        ]

        for formel, expected_error in invalid_cases:
            with self.subTest(formel=formel):
                resultat = kollaFormeln(formel)
                self.assertEqual(resultat, expected_error)


if __name__ == "__main__":
    unittest.main()
