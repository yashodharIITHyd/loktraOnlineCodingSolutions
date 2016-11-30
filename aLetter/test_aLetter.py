import unittest
from aLetterFunc import aLetterFunc

class Test_aLetter(unittest.TestCase):
    def test_one(self):
        self.assertTrue(abs(aLetterFunc(['a','a','b','d'],4,2)-0.8333)<=0.0001)

    def test_two(self):
        self.assertTrue(abs(aLetterFunc(['a','a','a','d'],4,2)-1)<=0.0001)

    def test_three(self):
        self.assertTrue(abs(aLetterFunc(['a','b','c','d','a'],5,2)-0.7)<=0.0001)

if __name__ == '__main__':
    unittest.main()