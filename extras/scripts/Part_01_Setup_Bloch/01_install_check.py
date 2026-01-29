# Import a module.
import os
# Import a module.
import sys
# Import specific names from a module.
from qiskit_ibm_runtime import QiskitRuntimeService

# Display output in the notebook or console.
print('Python:', sys.version)

# Assign a value to a variable.
token = os.getenv('QISKIT_IBM_TOKEN')
# Conditional branch.
if not token:
# Display output in the notebook or console.
    print('QISKIT_IBM_TOKEN is not set. Please set it in your environment.')
# Execute a statement.
    raise SystemExit(1)

# Display output in the notebook or console.
print('Token found. Saving account...')
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
# Display output in the notebook or console.
print('Account saved.')
