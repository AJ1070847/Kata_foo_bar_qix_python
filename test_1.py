import unittest 
from fractions import Fraction
from FooBarQix import *


class TestSum(unittest.TestCase):
    def test_foobar_verifer_no_divisble(self):
        """
        Test that verifies if a given number can be divided by 3 5 or 7 and return foo bar or qix in this case instead of the given number
        """
        data = 1
        result = foobar_verifer_divisble(data)
        self.assertEqual(result, "")
    
    def test_foobar_verifer_divisble_3(self):
        """
        Test that verifies if a given number can be divided by 3 5 or 7 and return foo bar or qix in this case instead of the given number
        """
        data = 3
        result = foobar_verifer_divisble(data)
        self.assertEqual(result, "Foo")
    
    def test_foobar_verifer_divisble_5(self):
        """
        Test that verifies if a given number can be divided by 3 5 or 7 and return foo bar or qix in this case instead of the given number
        """
        data = 5
        result = foobar_verifer_divisble(data)
        self.assertEqual(result, "Bar")
    
    def test_foobar_verifer_divisble_7(self):
        """
        Test that verifies if a given number can be divided by 3 5 or 7 and return foo bar or qix in this case instead of the given number
        """
        data = 7
        result = foobar_verifer_divisble(data)
        self.assertEqual(result, "Qix") 
    
    def test_foobar_verifie_contain_no(self):
        """
        Test that verifies if a given number contains 3 5 or 7 and return foo bar or qix in this case instead of the given number
        """
        data = 1
        result = foo_bar_verifier_presence(data)
        self.assertEqual(result, "")
    
    def test_foobar_verifie_contain_3(self):
        """
        Test that verifies if a given number contains 3 5 or 7 and return foo bar or qix in this case instead of the given number
        """
        data = 3
        result = foo_bar_verifier_presence(data)
        self.assertEqual(result, "Foo")

    def test_foobar_verifie_contain_5(self):
        """
        Test that verifies if a given number contains 3 5 or 7 and return foo bar or qix in this case instead of the given number
        """
        data = 5
        result = foo_bar_verifier_presence(data)
        self.assertEqual(result, "Bar")

    def test_foobar_verifie_contain_7(self):
        """
        Test that verifies if a given number contains 3 5  7 or 0 and return foo bar  qix or * in this case instead of the given number
        """
        data = 7
        result = foo_bar_verifier_presence(data)
        self.assertEqual(result, "Qix")
    
    def test_foobar_verifie_contain_7(self):
        """
        Test that verifies if a given number contains 3 5  7 or 0 and return foo bar  qix or * in this case instead of the given number
        """
        data = 101
        result = foo_bar_verifier_presence(data)
        self.assertEqual(result, "*")
    
    def test_foobar_verifie_contain_and_divid_no(self):
        """
        Test that verifies if a given number contains or can be divided by 3 5 or 7  and return True
        """
        data = 1
        result = foobar_verifier_changement(data)
        self.assertEqual(result, False)
    def test_foobar_verifie_contain_and_divid_true_divid(self):
        """
        Test that verifies if a given number contains or can be divided by 3 5 or 7  and return True
        """
        data = 9
        result = foobar_verifier_changement(data)
        self.assertEqual(result, True)
    def test_foobar_verifie_contain_and_divid_true_contains(self):
        """
        Test that verifies if a given number contains or can be divided by 3 5 or 7  and return True
        """
        data = 13
        result = foobar_verifier_changement(data)
        self.assertEqual(result, True)

    def test_foobar_final_result_33(self):
        """
        Test that verifies the final result
        """
        data = 33
        result = foor_bar_resultat_final(data)
        self.assertEqual(result, "FooFooFoo")
    def test_foobar_final_result_101(self):
        """
        Test that verifies the final result
        """
        data = 101
        result = foor_bar_resultat_final(data)
        self.assertEqual(result, "1*1")

if __name__=='__main__':
    unittest.main()