# Contributing

Thanks for considering a contribution to Federated Learning Simulation.

## Good contribution ideas

- Improve the notebook explanations.
- Add another small open dataset.
- Add non-IID client partitioning.
- Add client dropout simulation.
- Add client weighting experiments.
- Add secure-aggregation or differential-privacy demonstrations.
- Improve the Django visualization.
- Add tests for the federated averaging logic.

## Development setup

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

For optional PySyft experimentation:

```bash
python -m pip install -r requirements-optional.txt
```

## Pull requests

1. Keep changes focused.
2. Avoid adding large datasets or generated model binaries.
3. Keep the notebook runnable on a normal CPU.
4. Explain important changes in the pull request.
5. Update `CHANGELOG.md` when the change affects users.
