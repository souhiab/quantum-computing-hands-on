# Import specific names from a module.
from qiskit import QuantumCircuit
# Import specific names from a module.
from qiskit.primitives import Sampler
# Import specific names from a module.
from qiskit.visualization import plot_histogram

# Assign a value to a variable.
qc = QuantumCircuit(2, 2)
# Call a function or method.
qc.h(0)
# Call a function or method.
qc.cx(0, 1)
# Call a function or method.
qc.measure([0, 1], [0, 1])

# Assign a value to a variable.
sampler = Sampler()
# Assign a value to a variable.
result = sampler.run([qc], shots=2048).result()
# Assign a value to a variable.
quasi = result.quasi_dists[0]

# Assign a value to a variable.
counts = {k: int(v * 2048) for k, v in quasi.items()}
# Display output in the notebook or console.
print('Counts:', counts)
# Call a function or method.
plot_histogram(counts)
