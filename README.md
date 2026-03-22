# Python CI Testing Case Study

This repository is a small Python interview exercise focused on reading unfamiliar code, adding one meaningful unit test, and making CI pass.

## Setup

```bash
python -m pip install -e .[dev]
```

## Task

You are given a small Python package containing astronomy-flavoured utility functions and a basic GitHub Actions workflow.

Your task is to:

1. Read the code and identify how the existing test setup works.
2. Write one new unit test for `filter_sources_in_cone(...)` in `src/ci_case_study/coordinates.py`.
3. Make sure the test checks a meaningful behaviour or edge case.
4. Update the CI workflow only if needed so tests run on `push` and `pull_request`.
5. Ensure the repository reaches at least `85%` line coverage.

You do not need to add new features or refactor the package unless required to make the test pass.

Please include a short note in your submission explaining:

- what behaviour your test checks
- why you chose that case
- how you verified it

## Run The Checks

```bash
python -m pytest -q
python -m pytest --cov=src/ci_case_study --cov-report=term-missing
```

The first command should pass on the starter repository. The second command shows the current line coverage so you can confirm that your submission reaches the required threshold.

## Bonus

Add a second GitHub Actions workflow that builds the Docker image and pushes it to `ttl.sh/<unique-name>:1h`.
