import unittest
from examples.grover import build_grover_circuit

class TestGrover(unittest.TestCase):
    def test_grover_circuit(self):
        target = "1010"
        qc = build_grover_circuit(target)
        # Check that the circuit has measurement operations.
        self.assertTrue(qc.count_ops().get("measure", 0) > 0, "Circuit should include measurements.")

if __name__ == '__main__':
    unittest.main()
