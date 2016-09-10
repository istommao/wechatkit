#!/bin/bash

export PYTHONPATH=.
set -e

if [ -f htmlcov ]; then
    rm -r htmlcov
fi

py.test --cov=. --cov-report=html
