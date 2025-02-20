import unittest
from examples.bb84 import simulate_bb84

class TestBB84(unittest.TestCase):
    def test_bb84_shared_key(self):
        sender_bits, sender_bases, receiver_bases, measurements, shared_key = simulate_bb84(n=16)
        # Shared key should be a subset of sender bits where bases match.
        for i, (s_basis, r_basis) in enumerate(zip(sender_bases, receiver_bases)):
            if s_basis == r_basis:
                self.assertIn(sender_bits[i], [0, 1])

if __name__ == '__main__':
    unittest.main()
