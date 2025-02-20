"""
Quantum Random Number Generation (QRNG) Starter Kit

This script demonstrates how to generate quantum random bits using IonQ's simulator via Qiskit.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit_ionq import IonQProvider

# Initialize the IonQ provider (ensure IONQ_API_KEY is set in your environment)
provider = IonQProvider()
backend = provider.get_backend("simulator")

def quantum_random_bit(shots=1024):
    """
    Generate a quantum random bit by putting a qubit in superposition.
    
    Args:
        shots (int): Number of shots to run for statistical sampling.
    
    Returns:
        int: A random bit (0 or 1).
    """
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    
    job = backend.run(qc, shots=shots)
    counts = job.get_counts()
    
    bits = []
    for outcome, count in counts.items():
        bits.extend([int(outcome)] * count)
    return np.random.choice(bits)

if __name__ == "__main__":
    # Generate a sequence of 16 quantum random bits
    random_bits = [quantum_random_bit() for _ in range(16)]
    print("Quantum Random Bits:", random_bits)
