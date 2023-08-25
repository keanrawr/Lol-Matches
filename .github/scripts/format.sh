#!/bin/bash
set -e

poetry install

poetry run black lol_matches --check
