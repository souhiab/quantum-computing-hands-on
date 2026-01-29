# Import specific names from a module.
from qiskit import QuantumCircuit
# Import specific names from a module.
from qiskit.primitives import Sampler

# Define a function.
def encode_message(qc, msg):
# Conditional branch.
    if msg == '00':
# Execute a statement.
        pass
# Conditional branch.
    elif msg == '01':
# Call a function or method.
        qc.z(0)
# Conditional branch.
    elif msg == '10':
# Call a function or method.
        qc.x(0)
# Conditional branch.
    elif msg == '11':
# Call a function or method.
        qc.x(0)
# Call a function or method.
        qc.z(0)
# Conditional branch.
    else:
# Execute a statement.
        raise ValueError('Message must be 00, 01, 10, or 11')

# Define a function.
def superdense_coding(msg):
# Assign a value to a variable.
    qc = QuantumCircuit(2, 2)
# Call a function or method.
    qc.h(0)
# Call a function or method.
    qc.cx(0, 1)
# Call a function or method.
    encode_message(qc, msg)
# Call a function or method.
    qc.cx(0, 1)
# Call a function or method.
    qc.h(0)
# Call a function or method.
    qc.measure([0, 1], [0, 1])
# Execute a statement.
    return qc

# Assign a value to a variable.
sampler = Sampler()
# Loop over items.
for msg in ['00', '01', '10', '11']:
# Assign a value to a variable.
    qc = superdense_coding(msg)
# Assign a value to a variable.
    result = sampler.run([qc], shots=1024).result()
# Assign a value to a variable.
    counts = {k: int(v * 1024) for k, v in result.quasi_dists[0].items()}
# Display output in the notebook or console.
    print('Message', msg, '-> counts', counts)
