# Import a module.
import os
# Import a module.
import sys
# Import a module.
import importlib

# Display output in the notebook or console.
print('Python:', sys.version)

# Assign a value to a variable.
required = [
# Execute a statement.
    'qiskit',
# Execute a statement.
    'qiskit_ibm_runtime',
# Execute a statement.
    'matplotlib',
# Execute a statement.
    'numpy',
# Execute a statement.
    'sympy',
# Execute a statement.
    'pylatexenc',
# Execute a statement.
    'seaborn',
# Execute a statement.
    'pandas',
# Execute a statement.
]

# Loop over items.
for mod in required:
# Execute a statement.
    try:
# Call a function or method.
        importlib.import_module(mod)
# Display output in the notebook or console.
        print('OK:', mod)
# Execute a statement.
    except Exception as exc:
# Display output in the notebook or console.
        print('MISSING:', mod, '-', exc)

# Assign a value to a variable.
token = os.getenv('QISKIT_IBM_TOKEN')
# Conditional branch.
if token:
# Display output in the notebook or console.
    print('QISKIT_IBM_TOKEN is set (length:', len(token), ')')
# Conditional branch.
else:
# Display output in the notebook or console.
    print('QISKIT_IBM_TOKEN is NOT set')

# Display output in the notebook or console.
print('Healthcheck complete.')
