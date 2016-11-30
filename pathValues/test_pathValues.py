import unittest
from pathValuesFunc import pathValuesFunc

class Test_aLetter(unittest.TestCase):
    def test_one(self):
        edgesList=[
            "1 2","2 3","3 4"
        ]
        self.assertEqual(pathValuesFunc(4,3,edgesList,1),"6 12 18")

    def test_two(self):
        edgesList=[

        ]
        self.assertEqual(pathValuesFunc(4,0,edgesList,1),"-1 -1 -1")

    def test_three(self):
        edgesList=[
            "1 2","1 3","1 7","2 4","2 5","3 6","7 8"
        ]
        self.assertEqual(pathValuesFunc(8,7,edgesList,1),"6 6 12 12 12 6 12")
if __name__ == '__main__':
    unittest.main()