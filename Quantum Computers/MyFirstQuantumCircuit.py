import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Making a Quantum Circuit

# 1) A quantum circuit for preparing the quantum state |000> + i |111> / √2
circuit = QuantumCircuit(3)

circuit.h(0)           	 # generate new superposition
circuit.p(np.pi / 2, 0)	 # Generate new quantum phase
circuit.cx(0, 1)             # 0th-qubit-Controlled-NOT gate on 1st qubit
circuit.cx(0, 2)             # 0th-qubit-Controlled-NOT gate on 2nd qubit

# 2) Add the classical output in the form of measurement of all qubits
circuitMeasured = circuit.measure_all(inplace=False)

# 3) Execute using sampler position
sampler = StatevectorSampler()
job = sampler.run([circuitMeasured], shots=1000)
result = job.result()
print(f" > Counts {result[0].data['meas'].get_counts()}")
