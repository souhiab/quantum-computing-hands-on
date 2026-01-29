# Import a module.
import os
# Import specific names from a module.
from qiskit import QuantumCircuit
# Import specific names from a module.
from qiskit.primitives import Sampler
# Import specific names from a module.
from qiskit.visualization import plot_histogram
# Import specific names from a module.
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2, Session

# Bell state circuit
# Assign a value to a variable.
qc = QuantumCircuit(2, 2)
# Call a function or method.
qc.h(0)
# Call a function or method.
qc.cx(0, 1)
# Call a function or method.
qc.measure([0, 1], [0, 1])

# Simulator
# Assign a value to a variable.
sampler = Sampler()
# Assign a value to a variable.
result = sampler.run([qc], shots=1024).result()
# Assign a value to a variable.
sim_counts = {k: int(v * 1024) for k, v in result.quasi_dists[0].items()}
# Display output in the notebook or console.
print('Simulator counts:', sim_counts)
# Call a function or method.
plot_histogram(sim_counts)

# QPU
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

# Execute a statement.
with Session(service=service, backend=backend) as session:
# Assign a value to a variable.
    sampler2 = SamplerV2(session=session)
# Assign a value to a variable.
    job = sampler2.run([qc], shots=1024)
# Display output in the notebook or console.
    print('Job ID:', job.job_id())
# Assign a value to a variable.
    result2 = job.result()

# Assign a value to a variable.
qpu_counts = {k: int(v * 1024) for k, v in result2.quasi_dists[0].items()}
# Display output in the notebook or console.
print('QPU counts (approx):', qpu_counts)
# Call a function or method.
plot_histogram(qpu_counts)
