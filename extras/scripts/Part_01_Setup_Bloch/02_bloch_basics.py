# Import specific names from a module.
from math import pi
# Import specific names from a module.
from qiskit import QuantumCircuit
# Import specific names from a module.
from qiskit.quantum_info import Statevector
# Import specific names from a module.
from qiskit.visualization import plot_bloch_multivector

# Define a function.
def show_state(label, circuit):
# Assign a value to a variable.
    state = Statevector.from_instruction(circuit)
# Display output in the notebook or console.
    print(label, state)
# Call a function or method.
    plot_bloch_multivector(state)

# |0>
# Assign a value to a variable.
qc0 = QuantumCircuit(1)
# Call a function or method.
show_state('|0>', qc0)

# |1>
# Assign a value to a variable.
qc1 = QuantumCircuit(1)
# Call a function or method.
qc1.x(0)
# Call a function or method.
show_state('|1>', qc1)

# |+> = H|0>
# Assign a value to a variable.
qcp = QuantumCircuit(1)
# Call a function or method.
qcp.h(0)
# Call a function or method.
show_state('|+>', qcp)

# Rotated state Ry(pi/3)|0>
# Assign a value to a variable.
qcr = QuantumCircuit(1)
# Call a function or method.
qcr.ry(pi/3, 0)
# Call a function or method.
show_state('Ry(pi/3)|0>', qcr)
