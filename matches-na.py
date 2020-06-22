import os
import json
import boto3
import logging
from riotwatcher import LolWatcher
from utils import get_general_stats, get_team_stats, get_participants_stats

write_path = os.getenv('LOL_WRITE_PATH')
api_key = os.getenv('LOL_API_KEY')
watcher = LolWatcher(api_key)
region = 'na1'
match_id = 2868055755

# logging params
log_path = os.path.join(write_path, 'logs', 'na.log')
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)

# aws params
s3 = boto3.client('s3')

# infinite loop
while True:
    try:
        match = watcher.match.by_id(region, match_id)
        general_stats = get_general_stats(match)
        teams_stats = get_team_stats(match)
        participant_stats = get_participants_stats(match)

        match_stats = {**general_stats, **teams_stats, **participant_stats}

        # save to s3
        json_path = os.path.join('lol', 'matches', 'na', f'{match_id}.json')
        json_stats = json.dumps(match_stats)
        s3.put_object(Body=json_stats, Bucket='kean-analytics', Key=json_path)
        logging.info(f'Saved match data for match id:{match_id}')
    except:
        logging.error(f'Failed to fetch data for match id:{match_id}')
    match_id += 1
