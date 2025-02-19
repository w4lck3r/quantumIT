import os
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Options, Sampler
from dotenv import load_dotenv

# Charger la clé API depuis .env
load_dotenv()
API_KEY = os.getenv("IBM_QUANTUM_API_KEY")

if not API_KEY:
    raise ValueError("Veuillez ajouter votre clé API IBM Quantum dans le fichier .env")

# Se connecter à IBM Quantum
try:
    QiskitRuntimeService.save_account(channel="ibm_quantum", token=API_KEY, overwrite=True)
    service = QiskitRuntimeService()
    backends = service.backends()

    if not backends:
        raise ValueError("Aucun backend disponible. Vérifiez votre connexion à IBM Quantum.")

    # Vérifier si 'ibm_brisbane' est disponible
    backend_name = "ibm_brisbane"  # Changer avec 'ibm_kyiv' ou 'ibm_sherbrooke' si vous préférez
    available_backends = [backend.name for backend in backends]

    if backend_name not in available_backends:
        raise ValueError(f"Le backend '{backend_name}' n'est pas disponible. Backends disponibles : {available_backends}")

    backend = service.backend(backend_name)
except Exception as e:
    raise RuntimeError(f"Erreur de connexion à IBM Quantum : {e}")

# Créer un circuit quantique simple
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Configurer les options
options = Options()
options.update_options(shots=1024)  # Définir le nombre de shots

# Créer une session et exécuter le circuit avec le Sampler
with Session(backend=backend) as session:
    sampler = Sampler(session=session, options=options)
    job = sampler.run(qc)
    result = job