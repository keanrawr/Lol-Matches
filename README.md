![pytest](https://github.com/keanrawr/Lol-Matches/workflows/pytest/badge.svg)

# Lol Predictions

So, I'm a big league of legends fan, I don't play as much as I'd like but I like to think that I have mildly good instincts to guess the winner in a professional match. However, as a data scientist I think that it's very possible to create a model to predict a match outcome.

My initial "predict lol matches" google search yielded some interesting results, the one that caught my eye is an implementation that uses a [ranked matches kagle dataset](https://www.kaggle.com/paololol/league-of-legends-ranked-matches), and uses xgboost and shap to both fit a model and explain it. [Here's the reference notebook](https://slundberg.github.io/shap/notebooks/League%20of%20Legends%20Win%20Prediction%20with%20XGBoost.html).

Since my go-to programming language is python, the implementation is in python.

# About the repo

I'm trying to be more organized and leave the tedious stuff to other tools, that's why this project uses [poetry](https://python-poetry.org/) to handle dependency management.

One nice thing about poetry is that it can run scripts really easy, like the very simple tests currently implemented.


## Setting up the project

To setup the project you need to have poetry in your system, since I'm on mac, my prefered way to do it is using [homebrew](https://brew.sh/).

```
# use homebrew to install poetry
brew install poetry

# install the dependencies
poetry install

# run tests
poetry run pytest
```

## Data gathering

To gather match data there's a very simplified version of a "match scraper" (using quotes, because it's not really scraping). Most of the heavy lifting is done by the `riotwatcher` python package.

To use the `MatchScraper` class, you only need to set the environment variable `RIOT_API_KEY` to a valid riot API key, you can get a free 24 hour one from the [riot developer portal](https://developer.riotgames.com/), or submit a request for a long-lived key.

The implementation in this repo is done in the `get_matches.py` module, currently this script runs inside a raspberry pi gathering data and saving it to an s3 bucket using the `S3Helper` class.

## Data processing

Currently three data sets are being saved to an s3 bucket: matches, teams and participants. Once the data is available in s3, databricks is used to process the raw data and save it to the s3 bucket again.

The data pipeline can be found in the `notebooks` directory, currently there's only one version of the dataset, but that's enough to get started.

## Prediction model (WIP)

So far this stage is in very early development, we're trying to accomplish a full end to end model deployment, and to acomplish it we'll be using [mlflow](https://mlflow.org/). We've setup an mlflow tracking server on aws using EC2, but that's mainly the fancy part.

For modeling we've though of submitting pull requests that train a model and report on model results, this to evaluate the performance of models and make a decision on which might be the right one for the job.
