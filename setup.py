from setuptools import setup, find_packages

setup(
    name="tenzro-q",
    version="0.1.0",
    description="Quantum-enhanced security starter kits for Tenzro",
    author="Tenzro Team",
    packages=find_packages(),
    install_requires=[
        "qiskit>=0.39.0",
        "qiskit-ionq",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
