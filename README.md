# Federated Learning Simulation

A lightweight, interview-ready simulation of **Federated Learning** using multiple simulated clients that train locally and share only model updates instead of raw training records.

The project demonstrates the core ideas behind federated learning:

- Multiple clients keep their own local partitions of data.
- Each client trains a small logistic-regression model locally.
- Only model parameters are exchanged with the coordinator.
- The coordinator performs **Federated Averaging (FedAvg)**.
- A global model is evaluated after every communication round.
- The Django demo turns the experiment into an interactive web application.
- PySyft is included as an optional extension path for privacy-preserving data governance and federated workflows.

## Why this project is lightweight

The notebook uses scikit-learn's built-in Breast Cancer Wisconsin dataset. It is small, already available through scikit-learn, and does not require a GPU, large model downloads, or a large dataset archive.

The core simulation uses NumPy, pandas and scikit-learn. This is intentional: current PySyft is a broader client/server privacy and data-governance platform, and forcing it into the minimum runnable path would make a CPU-only portfolio project unnecessarily heavy.

## Project structure

```text
Federated-Learning-Simulation/
├── notebooks/
│   └── federated_learning_simulation.ipynb
├── django_demo/
│   ├── manage.py
│   ├── federated_demo/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── wsgi.py
│   └── templates/
│       └── index.html
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTE.md
├── README.md
├── requirements.txt
└── requirements-optional.txt
```

There is intentionally **no `src` directory, preprocessing module, model module, or separate training script**. The notebook is the main implementation artifact.

## Run the notebook

Recommended Python: 3.12+

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
jupyter notebook
```

Open:

```text
notebooks/federated_learning_simulation.ipynb
```

The notebook:

1. Loads the small built-in dataset.
2. Standardizes the features.
3. Splits the training set among simulated clients.
4. Creates a local model for every client.
5. Trains clients without sharing their raw records.
6. Aggregates model weights with FedAvg.
7. Evaluates the global model.
8. Compares local-only and federated performance.
9. Visualizes accuracy across communication rounds.
10. Explains where PySyft can be introduced in a production design.

## Run the Django demo

```bash
cd django_demo
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

The page lets you choose the number of clients and communication rounds, then runs a lightweight federated simulation in the web request.

The web page credits:

- GitHub: https://github.com/InfinitePraveen
- LinkedIn: https://www.linkedin.com/in/infinitepraveen/

## Federated learning flow

```text
                  ┌──────────────────┐
                  │ Global Model     │
                  │ Coordinator      │
                  └────────┬─────────┘
                           │ global weights
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   ┌────────────┐   ┌────────────┐   ┌────────────┐
   │ Client 1   │   │ Client 2   │   │ Client N   │
   │ Local Data │   │ Local Data │   │ Local Data │
   └─────┬──────┘   └─────┬──────┘   └─────┬──────┘
         │ model update          │
         └──────────────┬────────┴──────────────┐
                        ▼
                 FedAvg Aggregation
                        │
                        ▼
                 Updated Global Model
```

### Important privacy note

Federated learning does **not automatically guarantee privacy**. This simulation demonstrates the architectural idea that raw client records remain local. A production system should additionally consider secure aggregation, differential privacy, encryption, authentication, access policies, and threat models.

## PySyft connection

PySyft is useful when the project needs a stronger privacy/data-governance layer around private datasets and remote computation. The optional requirements file keeps it separate from the lightweight demo:

```bash
python -m pip install -r requirements-optional.txt
```

The notebook includes a PySyft compatibility/check section and explains how the simulation can be mapped to a PySyft-based architecture.

## Interview talking points

**Problem:** Organizations may want to train a shared model while keeping sensitive data at hospitals, banks, phones, or branches.

**Solution:** Federated learning moves the model to the data. Clients train locally and send model updates to a coordinator.

**Aggregation:** FedAvg computes a weighted average of client parameters, typically weighted by each client's number of training samples.

**Trade-off:** Communication rounds, client drift, non-IID data, malicious updates, and privacy leakage are important practical challenges.

**Demo value:** The Django interface makes the distributed-learning process understandable to a non-technical interviewer while the notebook shows the actual ML implementation.

## License

This project is intended as an educational portfolio project. Dataset availability and third-party package licenses remain subject to their respective projects.
