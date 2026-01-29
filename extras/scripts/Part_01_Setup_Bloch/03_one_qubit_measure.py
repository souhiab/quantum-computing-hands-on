# Import specific names from a module.
from qiskit import QuantumCircuit
# Import specific names from a module.
from qiskit.primitives import Sampler
# Import specific names from a module.
from qiskit.visualization import plot_histogram

# Assign a value to a variable.
qc = QuantumCircuit(1, 1)
# Call a function or method.
qc.h(0)
# Call a function or method.
qc.measure(0, 0)

# Assign a value to a variable.
sampler = Sampler()
# Assign a value to a variable.
result = sampler.run([qc], shots=1024).result()
# Assign a value to a variable.
quasi = result.quasi_dists[0]

# Assign a value to a variable.
counts = {k: int(v * 1024) for k, v in quasi.items()}
# Display output in the notebook or console.
print('Counts:', counts)
# Call a function or method.
plot_histogram(counts)
