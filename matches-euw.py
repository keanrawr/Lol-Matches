import os
import json
import logging
from riotwatcher import LolWatcher
from utils import get_general_stats, get_team_stats, get_participants_stats

write_path = os.getenv('LOL_WRITE_PATH')
api_key = os.getenv('LOL_API_KEY')
watcher = LolWatcher(api_key)
region = 'euw1'
match_id = 3768193193

log_path = os.path.join(write_path, 'logs', 'euw.log')
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s %(name)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)

# infinite loop
while True:
    try:
        logging.info(f'Fetching data for match id:{match_id}')
        match = watcher.match.by_id(region, match_id)
        general_stats = get_general_stats(match)
        teams_stats = get_team_stats(match)
        participant_stats = get_participants_stats(match)

        match_stats = {**general_stats, **teams_stats, **participant_stats}

        json_path = os.path.join(write_path, 'matches', 'euw', f'{match_id}.json')
        with open(json_path, 'w') as f:
            json.dump(match_stats, f)
        logging.info(f'Saving match data for match id:{match_id}')
    except:
        logging.error(f'Failed to fetch data for match id:{match_id}')
    match_id += 1
