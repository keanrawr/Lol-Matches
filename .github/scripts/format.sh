#!/bin/bash
set -e

poetry install

poetry run black lol_matches --check
poetry run black tests --check
