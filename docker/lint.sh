#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_utility/ tests/

black democritus_utility/ tests/

mypy democritus_utility/ tests/

pylint --fail-under 9 democritus_utility/*.py

flake8 democritus_utility/ tests/

bandit -r democritus_utility/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_utility/ tests/
