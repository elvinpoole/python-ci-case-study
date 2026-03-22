# Python CI Case Study

This repository is a small Python interview exercise focused on reading unfamiliar code, adding one meaningful unit test, and making CI pass.

## Setup

```bash
python -m pip install -e .[dev]
```

To test the full GitHub Actions and deployment path, you will likely need your own GitHub account.

You may either:

- clone this repository and work locally
- fork it into your own GitHub account and work there

Use whichever approach you prefer.

## Task

You are given a small Python package containing astronomy-flavoured utility functions and a basic GitHub Actions workflow.

Your task is to:

1. Read the code and identify how the existing test setup works.
2. Write one new unit test for `filter_sources_in_cone(...)` in `src/ci_case_study/coordinates.py`.
3. Make sure the test checks a meaningful behaviour or edge case.
4. Update the existing GitHub Actions workflow so it verifies the code on `push` and `pull_request`, enforces at least `85%` line coverage, and publishes the Docker image to `ttl.sh`.

You do not need to add new features or refactor the package unless required to make the test pass.

Please include a short note in your submission explaining:

- what behaviour your test checks
- why you chose that case
- how you verified it

## Run The Checks

```bash
python -m pytest -q
```

The starter repository should pass this command before you begin.
