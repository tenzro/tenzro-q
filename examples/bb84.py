#!/usr/bin/env python
"""
BB84 Quantum Key Distribution (QKD) Simulation Starter Kit

This script simulates a simplified round of the BB84 protocol using IonQ's simulator.
"""

import random
from qiskit import QuantumCircuit
from qiskit_ionq import IonQProvider

provider = IonQProvider()
backend = provider.get_backend("simulator")

def bb84_round(bit, sender_basis, receiver_basis):
    """
    Simulate one round of BB84 protocol.
    
    Args:
        bit (int): Bit (0 or 1) to send.
        sender_basis (str): 'Z' (standard) or 'X' (Hadamard) basis for preparation.
        receiver_basis (str): 'Z' or 'X' basis for measurement.
    
    Returns:
        int: Measurement outcome.
    """
    qc = QuantumCircuit(1, 1)
    
    # Encode the bit
    if bit == 1:
        qc.x(0)
    if sender_basis == 'X':
        qc.h(0)
    
    # Receiver measurement
    if receiver_basis == 'X':
        qc.h(0)
    
    qc.measure(0, 0)
    job = backend.run(qc, shots=1)
    result = job.get_counts()
    outcome = int(list(result.keys())[0])
    return outcome

def simulate_bb84(n=16):
    sender_bits = [random.randint(0, 1) for _ in range(n)]
    sender_bases = [random.choice(['Z', 'X']) for _ in range(n)]
    receiver_bases = [random.choice(['Z', 'X']) for _ in range(n)]
    
    measurement_results = []
    for bit, s_basis, r_basis in zip(sender_bits, sender_bases, receiver_bases):
        measured = bb84_round(bit, s_basis, r_basis)
        measurement_results.append(measured)
    
    # Form shared key only when bases match
    shared_key = [bit for bit, s_basis, r_basis in zip(sender_bits, sender_bases, receiver_bases)
                  if s_basis == r_basis]
    
    return sender_bits, sender_bases, receiver_bases, measurement_results, shared_key

if __name__ == "__main__":
    sender_bits, sender_bases, receiver_bases, measurement_results, shared_key = simulate_bb84(16)
    print("Sender bits:        ", sender_bits)
    print("Sender bases:       ", sender_bases)
    print("Receiver bases:     ", receiver_bases)
    print("Measurement results:", measurement_results)
    print("Shared key (matching bases):", shared_key)
