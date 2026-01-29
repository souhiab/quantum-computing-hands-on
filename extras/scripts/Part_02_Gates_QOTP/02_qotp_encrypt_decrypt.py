# Import a module.
import random
# Import specific names from a module.
from qiskit import QuantumCircuit
# Import specific names from a module.
from qiskit.quantum_info import Statevector

# Assign a value to a variable.
a = random.randint(0, 1)
# Assign a value to a variable.
b = random.randint(0, 1)
# Display output in the notebook or console.
print('Random key bits a, b:', a, b)

# Prepare a simple state |+>
# Assign a value to a variable.
qc = QuantumCircuit(1)
# Call a function or method.
qc.h(0)
# Assign a value to a variable.
original = Statevector.from_instruction(qc)

# Encrypt with X^a Z^b
# Conditional branch.
if a == 1:
# Call a function or method.
    qc.x(0)
# Conditional branch.
if b == 1:
# Call a function or method.
    qc.z(0)

# Decrypt with Z^b X^a
# Conditional branch.
if b == 1:
# Call a function or method.
    qc.z(0)
# Conditional branch.
if a == 1:
# Call a function or method.
    qc.x(0)

# Assign a value to a variable.
final = Statevector.from_instruction(qc)
# Assign a value to a variable.
fidelity = abs(original.data.conjugate().dot(final.data)) ** 2
# Display output in the notebook or console.
print('Fidelity after decrypt:', fidelity)
