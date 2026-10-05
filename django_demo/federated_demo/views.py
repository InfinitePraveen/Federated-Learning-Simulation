from django.shortcuts import render

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def _fedavg_demo(n_clients=4, rounds=6):
    dataset = load_breast_cancer()
    X = dataset.data
    y = dataset.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        stratify=y,
        random_state=42,
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    rng = np.random.default_rng(42)
    indices = np.arange(len(X_train))
    rng.shuffle(indices)
    partitions = np.array_split(indices, n_clients)

    client_data = [
        (X_train[idx], y_train[idx])
        for idx in partitions
    ]

    history = []

    for round_number in range(1, rounds + 1):
        updates = []

        for X_local, y_local in client_data:
            model = LogisticRegression(
                max_iter=300,
                solver="liblinear",
                random_state=42,
            )
            model.fit(X_local, y_local)
            updates.append(
                (model.coef_.copy(), model.intercept_.copy(), len(X_local))
            )

        total = sum(item[2] for item in updates)

        global_coef = sum(
            (n / total) * coef for coef, _, n in updates
        )
        global_intercept = sum(
            (n / total) * intercept for _, intercept, n in updates
        )

        scores = X_test @ global_coef.T + global_intercept
        predictions = (scores.ravel() >= 0).astype(int)
        accuracy = accuracy_score(y_test, predictions)

        history.append(
            {
                "round": round_number,
                "accuracy": round(accuracy, 4),
            }
        )

    return history


def home(request):
    try:
        n_clients = int(request.GET.get("clients", "4"))
    except ValueError:
        n_clients = 4

    try:
        rounds = int(request.GET.get("rounds", "6"))
    except ValueError:
        rounds = 6

    n_clients = min(max(n_clients, 2), 8)
    rounds = min(max(rounds, 1), 12)

    history = _fedavg_demo(n_clients=n_clients, rounds=rounds)

    context = {
        "history": history,
        "clients": n_clients,
        "rounds": rounds,
        "final_accuracy": history[-1]["accuracy"],
        "github": "https://github.com/InfinitePraveen",
        "linkedin": "https://www.linkedin.com/in/infinitepraveen/",
    }
    return render(request, "index.html", context)
