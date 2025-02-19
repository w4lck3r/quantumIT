# Quantum Computing with IBM Quantum and Qiskit Runtime

This project demonstrates how to connect to IBM Quantum's backend using the `qiskit_ibm_runtime` package, create a simple quantum circuit, and execute it on a real quantum computer.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Script](#running-the-script)
5. [Output](#output)
6. [Troubleshooting](#troubleshooting)
---

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.8 or higher**: The script is written in Python and requires a compatible version.
2. **IBM Quantum API Key**: You need an API key from IBM Quantum. Sign up at [IBM Quantum](https://quantum-computing.ibm.com/) if you don't have an account.
3. **Qiskit and Qiskit Runtime**: Install the required Python packages.

---

## Installation

1. Clone this repository or download the script to your local machine.
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install the required dependencies:
    ```bash
    pip install qiskit qiskit-ibm-runtime python-dotenv
    ````
## Configuration
1. Set Up Your API Key:
* Create a .env file in the root directory of your project.
* Add your IBM Quantum API key to the .env file:
    ```bash
        IBM_QUANTUM_API_KEY=your_api_key_here
    ```
* Replace your_api_key_here with your actual API key.

* Choose a Backend:

    * The script is configured to use the ibm_brisbane backend by default. You can change this to another backend (e.g., ibm_kyiv or ibm_sherbrooke) by modifying the backend_name variable in the script.
## Running the Script

1. Activate your virtual environment (if you created one) :
    ```bash
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
2. Run the script :
    ```bash
    python Script.py
    ```
## Output
* json output file :

    ```bash
            
        "id": "cyv25zz78z600082q6v0",
        "backend_name": "ibm_brisbane",
        "mode": "dedicated",
        "interactive_ttl": 2,
        "max_ttl": 900,
        "active_ttl": 900,
        "accepting_jobs": false,
        "created_at": "2025-02-19T18:29:19.939Z",
        "closed_at": "2025-02-19T18:29:20.891Z",
        "state": "closed",
        "elapsed_time": 0
        
    ```

## Troubleshooting
### Common Issues

1. API Key Not Found:

    *  Ensure the .env file is in the correct directory and contains the IBM_QUANTUM_API_KEY variable.

    * Verify that the python-dotenv package is installed.

2. Backend Not Available:

    * Check the list of available backends by printing available_backends in the script.

    * Ensure the backend you are trying to use is operational and not under maintenance.

3. AttributeError: 'OptionsV2' object has no attribute 'execution':

    * This error occurs if you are using an outdated version of the qiskit_ibm_runtime package. Update your package and follow the migration guide: Qiskit Runtime Migration Guide.

4. Job Fails to Execute:

    * Check the job status using the job ID on the IBM Quantum dashboard.

    * Ensure your circuit is compatible with the selected backend.