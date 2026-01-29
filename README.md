# Hands-On Experience Implementing Quantum Computing

A 3-hour workshop for absolute beginners using VS Code notebooks.

## What We Will Do (3 Hours)

- Verify VS Code + Python and create a clean virtual environment
- Install Qiskit and the IBM Runtime tools
- Visualize single-qubit states on the Bloch sphere
- Build and measure circuits (1 and 2 qubits)
- Run a Bell circuit on a real IBM QPU
- Use basic gates and a simple quantum one-time pad
- Compare simulator vs QPU and perform superdense coding

## File Tree

```text
hands-on-qpu-workshop/
  README.md
  requirements.txt
  .gitignore
  LICENSE
  .env.example
  docs/
    GLOSSARY.md
  extras/
    scripts/
  Part_00_VSCode_Python_Setup/
    README.md
    notebooks/
      00_vscode_python_check.ipynb
  Part_01_Setup_Bloch/
    README.md
    notebooks/
      01_setup_bloch.ipynb
    run_as_script.py
  Part_02_Gates_QOTP/
    README.md
    notebooks/
      02_gates_qotp.ipynb
    run_as_script.py
  Part_03_Entanglement_Superdense/
    README.md
    notebooks/
      03_entanglement_superdense.ipynb
    run_as_script.py
```

## Prerequisites (VS Code + Python)

- Install VS Code
- Install Python 3.10 or newer
- VS Code extensions: **Python** and **Jupyter**

Verify your setup in Part 00.

## Install Qiskit + IBM Runtime

```powershell
cd "d:\PHYSIQUE MATHEMATIQUE\doctora\last year\PWF_IBM_MOROCCO\hands-on-qpu-workshop"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

```bash
cd "d:\PHYSIQUE MATHEMATIQUE\doctora\last year\PWF_IBM_MOROCCO\hands-on-qpu-workshop"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## VS Code Interpreter Selection

- Open the command palette in VS Code
- Select **Python: Select Interpreter**
- Choose `.venv` for this project

## IBM Token (QISKIT_IBM_TOKEN)

- Set `QISKIT_IBM_TOKEN` as an environment variable
- Optional: save credentials using `QiskitRuntimeService.save_account`
- Note: saved credentials can be stored in plain text. Only save on trusted machines.

## Run the Notebooks (in order)

1) `Part_00_VSCode_Python_Setup/notebooks/00_vscode_python_check.ipynb`
2) `Part_01_Setup_Bloch/notebooks/01_setup_bloch.ipynb`
3) `Part_02_Gates_QOTP/notebooks/02_gates_qotp.ipynb`
4) `Part_03_Entanglement_Superdense/notebooks/03_entanglement_superdense.ipynb`

## Troubleshooting

- **python not found**: install Python and restart VS Code
- **pip not found**: run `python -m ensurepip --upgrade`
- **wrong interpreter**: select `.venv` in VS Code
- **token missing**: set `QISKIT_IBM_TOKEN` and restart the kernel

## References

- VS Code Python and Jupyter documentation
- Qiskit installation guide and runtime documentation

## Hashtags / Topics

#QuantumComputing #Qiskit #IBMQuantum #QPU #HandsOn #Workshop #Beginner #BlochSphere #QuantumGates #Entanglement #SuperdenseCoding #QuantumCryptography
