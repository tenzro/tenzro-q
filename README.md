# tenzro-q

**tenzro-q** is a repository dedicated to exploring quantum-enhanced security concepts within the Tenzro ecosystem. This project includes starter kits for:
- Quantum Random Number Generation (QRNG)
- Simulated Quantum Key Distribution (BB84)
- Grover's Algorithm for Cryptographic Validation

These examples use Qiskit with the IonQ provider to demonstrate how quantum computing techniques can be applied for cryptographic applications such as secure key generation, quantum-resistant protocols, and simulation of quantum attacks.

## Features

- **QRNG:** Generate high-quality random numbers using quantum superposition.
- **BB84 Simulation:** A simplified implementation of the BB84 quantum key distribution protocol.
- **Grover’s Algorithm:** Prototype to simulate quantum search for testing cryptographic strength.

## Getting Started

### Prerequisites

- Python 3.7+
- An IonQ API Key (set as the environment variable `IONQ_API_KEY`)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tenzro/tenzro-q.git
   cd tenzro-q
