import os
import json
from riotwatcher import LolWatcher
from utils import get_general_stats, get_team_stats, get_participants_stats

write_path = os.getenv('LOL_WRITE_PATH')
api_key = os.getenv('LOL_API_KEY')
watcher = LolWatcher(api_key)
region = 'euw1'
match_id = 3768193193



for i in range(5):
    match = watcher.match.by_id(region, match_id)
    general_stats = get_general_stats(match)
    teams_stats = get_team_stats(match)
    participant_stats = get_participants_stats(match)

    match_stats = {**general_stats, **teams_stats, **participant_stats}

    json_path = os.path.join(write_path, 'matches', 'euw', f'{match_id}.json')
    with open(json_path, 'w') as f:
        json.dump(match_stats, f, indent=2)

    match_id += 1
    print(f'Finished for iter {i}')
