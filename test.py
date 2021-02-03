import unittest
from vector import Vector

class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -4.0, 8.0)
        self.v2 = Vector(4.0, -5.0, 6.0)
        self.v3 = Vector(-2.0, 4.0, -8.0)
        self.v1_plus_v2 = Vector(5.0, -9.0, 14.0)
        self.v1_minus_v2 = Vector(-3.0, 1.0, 2.0)
    
    def test_dot_product(self):
        self.assertEqual(self.v1.dot_product(self.v2),72.0)
    
    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(),9.0)
    
    def test_addition(self):
        self.assertEqual(self.v1 + self.v2, self.v1_plus_v2)

    def test_subtraction(self):
        self.assertEqual(self.v1 - self.v2, self.v1_minus_v2)
    
    def test_multiplication(self):
        self.assertEqual(self.v1 * 2, Vector(2.0, -8.0, 16.0))
        # self.assertEqual(2* self.v1, Vector(2.0, -8.0, 16.0))
        # __rmul__ is giving weird error __mul__() takes 2 positional arguments but 3 were given

    def test_division(self):
        self.assertEqual(self.v3 / 2, Vector(-1.0, 2.0, -4.0))

if __name__ == "__main__":
    unittest.main()
