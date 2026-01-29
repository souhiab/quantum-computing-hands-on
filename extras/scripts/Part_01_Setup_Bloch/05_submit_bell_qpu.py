# Import a module.
import os
# Import specific names from a module.
from qiskit import QuantumCircuit
# Import specific names from a module.
from qiskit.visualization import plot_histogram
# Import specific names from a module.
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2, Session

# Assign a value to a variable.
token = os.getenv('QISKIT_IBM_TOKEN')
# Conditional branch.
if not token:
# Display output in the notebook or console.
    print('QISKIT_IBM_TOKEN is not set. Skipping QPU run.')
# Execute a statement.
    raise SystemExit(0)

# Call a function or method.
QiskitRuntimeService.save_account(
# Assign a value to a variable.
    channel='ibm_quantum',
# Assign a value to a variable.
    token=token,
# Assign a value to a variable.
    overwrite=True
# Execute a statement.
)

# Assign a value to a variable.
service = QiskitRuntimeService(channel='ibm_quantum')
# Assign a value to a variable.
backend = service.least_busy(simulator=False, operational=True)
# Display output in the notebook or console.
print('Using backend:', backend.name)

# Assign a value to a variable.
qc = QuantumCircuit(2, 2)
# Call a function or method.
qc.h(0)
# Call a function or method.
qc.cx(0, 1)
# Call a function or method.
qc.measure([0, 1], [0, 1])

# Execute a statement.
with Session(service=service, backend=backend) as session:
# Assign a value to a variable.
    sampler = SamplerV2(session=session)
# Assign a value to a variable.
    job = sampler.run([qc], shots=1024)
# Display output in the notebook or console.
    print('Job ID:', job.job_id())
# Assign a value to a variable.
    result = job.result()

# Assign a value to a variable.
quasi = result.quasi_dists[0]
# Assign a value to a variable.
counts = {k: int(v * 1024) for k, v in quasi.items()}
# Display output in the notebook or console.
print('Counts (approx):', counts)
# Call a function or method.
plot_histogram(counts)
