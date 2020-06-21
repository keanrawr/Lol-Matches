# Lol Predictions

So, I'm a big league of legends fan, I don't play as much as I'd like but I like to think that I have mildly good instincts to guess the winner in a professional match. However, as a data scientist I think that it's very possible to create a model to predict a match outcome. As of June 2020 I haven't done much research on the subject, except for the initial "predict lol matches" google search.

Since my go-to programming language is python, the implementation will be in python.

# About the repo

There are two parts for the repo:

1. Data gathering
2. Prediction modeling

## Data gathering

We'll be using the `riotwatcher` python package. There are two environment values that need to be specified, `LOL_WRITE_PATH` is the path where the data should be written to, we did it this way to ensure that the code will work in both development and "production" environments. `LOL_API_KEY` is the Riot API key that we got from the developer portal.
