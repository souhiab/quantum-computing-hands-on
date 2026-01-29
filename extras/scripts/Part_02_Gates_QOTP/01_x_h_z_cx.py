# Import specific names from a module.
from qiskit import QuantumCircuit
# Import specific names from a module.
from qiskit.primitives import Sampler
# Import specific names from a module.
from qiskit.visualization import plot_histogram

# Single-qubit gates
# Assign a value to a variable.
qc1 = QuantumCircuit(1, 1)
# Call a function or method.
qc1.x(0)
# Call a function or method.
qc1.measure(0, 0)

# Assign a value to a variable.
sampler = Sampler()
# Assign a value to a variable.
result = sampler.run([qc1], shots=1024).result()
# Assign a value to a variable.
counts = {k: int(v * 1024) for k, v in result.quasi_dists[0].items()}
# Display output in the notebook or console.
print('X gate counts:', counts)
# Call a function or method.
plot_histogram(counts)

# Two-qubit CX
# Assign a value to a variable.
qc2 = QuantumCircuit(2, 2)
# Call a function or method.
qc2.x(0)
# Call a function or method.
qc2.cx(0, 1)
# Call a function or method.
qc2.measure([0, 1], [0, 1])

# Assign a value to a variable.
result2 = sampler.run([qc2], shots=1024).result()
# Assign a value to a variable.
counts2 = {k: int(v * 1024) for k, v in result2.quasi_dists[0].items()}
# Display output in the notebook or console.
print('CX counts:', counts2)
# Call a function or method.
plot_histogram(counts2)
