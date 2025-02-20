import unittest
from examples.qrng import quantum_random_bit

class TestQRNG(unittest.TestCase):
    def test_random_bit(self):
        bit = quantum_random_bit(shots=256)
        self.assertIn(bit, [0, 1], "Generated bit should be 0 or 1")

if __name__ == '__main__':
    unittest.main()
