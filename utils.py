import time


def get_stat_value(match, *args):
    value = match
    for arg in args:
        value = value.get(arg)
    return value if value else ''


def create_key(val_name, *args):
    value = '_'.join(args)
    return val_name + '_' + value


def get_general_stats(match):
    create_dttm = get_stat_value(match, 'gameCreation')
    create_dttm = time.gmtime(create_dttm / 1000)
    create_dttm = time.strftime('%Y-%m-%d %H:%M:%S', create_dttm)
    return {
        'gameId': get_stat_value(match, 'gameId'),
        'platformId': get_stat_value(match, 'platformId'),
        'gameCreation': create_dttm,
        'gameDuration': get_stat_value(match, 'gameDuration'),
        'queueId': get_stat_value(match, 'queueId'),
        'mapId': get_stat_value(match, 'mapId'),
        'seasonId': get_stat_value(match, 'seasonId'),
        'gameVersion': get_stat_value(match, 'gameVersion'),
        'gameMode': get_stat_value(match, 'gameMode'),
        'gameType': get_stat_value(match, 'gameType')
    }


def get_team_stats(match):
    teams = match['teams']
    stats = dict()
    for team in teams:
        prefix = get_stat_value(team, 'teamId')
        if prefix == 100:
            blue_victory = 1 if get_stat_value(team, 'win') == 'Win' else 0
        # values for each variable
        firstBlood = get_stat_value(team, 'firstBlood')
        firstBlood = 1 if firstBlood else 0
        firstTower = get_stat_value(team, 'firstTower')
        firstTower = 1 if firstTower else 0
        firstInhibitor = get_stat_value(team, 'firstInhibitor')
        firstInhibitor = 1 if firstInhibitor else 0
        firstBaron = get_stat_value(team, 'firstBaron')
        firstBaron = 1 if firstBaron else 0
        firstDragon = get_stat_value(team, 'firstDragon')
        firstDragon = 1 if firstDragon else 0
        firstRiftHerald = get_stat_value(team, 'firstRiftHerald')
        firstRiftHerald = 1 if firstRiftHerald else 0
        towerKills = get_stat_value(team, 'towerKills')
        inhibitorKills = get_stat_value(team, 'inhibitorKills')
        baronKills = get_stat_value(team, 'baronKills')
        dragonKills = get_stat_value(team, 'dragonKills')
        riftHeraldKills = get_stat_value(team, 'riftHeraldKills')
        # key name for previous values
        firstBlood_key = f'firstBlood_{prefix}'
        firstTower_key = f'firstTower_{prefix}'
        firstInhibitor_key = f'firstInhibitor_{prefix}'
        firstBaron_key = f'firstBaron_{prefix}'
        firstDragon_key = f'firstDragon_{prefix}'
        firstRiftHerald_key = f'firstRiftHerald_{prefix}'
        towerKills_key = f'towerKills_{prefix}'
        inhibitorKills_key = f'inhibitorKills_{prefix}'
        baronKills_key = f'baronKills_{prefix}'
        dragonKills_key = f'dragonKills_{prefix}'
        riftHeraldKills_key = f'riftHeraldKills_{prefix}'
        # dictionary for current team
        iter_stats = {
            firstBlood_key: firstBlood,
            firstTower_key: firstTower,
            firstInhibitor_key: firstInhibitor,
            firstBaron_key: firstBaron,
            firstDragon_key: firstDragon,
            firstRiftHerald_key: firstRiftHerald,
            towerKills_key: towerKills,
            inhibitorKills_key: inhibitorKills,
            baronKills_key: baronKills,
            dragonKills_key: dragonKills,
            riftHeraldKills_key: riftHeraldKills
        }
        stats = {**stats, **iter_stats}
    return {'blue_victory': blue_victory, **stats}


def get_participants_stats(match):
    participants = match['participants']
    stats = dict()
    for part in participants:
        part_id = get_stat_value(part, 'participantId')
        team = get_stat_value(part, 'teamId')
        prefix = f'{team}_{part_id}'
        # values for each variable
        highestAchievedSeasonTier = get_stat_value(part, 'highestAchievedSeasonTier')
        championId = get_stat_value(part, 'championId')
        kills = get_stat_value(part, 'stats', 'kills')
        deaths = get_stat_value(part, 'stats', 'deaths')
        assists = get_stat_value(part, 'stats', 'assists')
        largestKillingSpree = get_stat_value(part, 'stats', 'largestKillingSpree')
        largestMultiKill = get_stat_value(part, 'stats', 'largestMultiKill')
        killingSprees = get_stat_value(part, 'stats', 'killingSprees')
        longestTimeSpentLiving = get_stat_value(part, 'stats', 'longestTimeSpentLiving')
        doubleKills = get_stat_value(part, 'stats', 'doubleKills')
        tripleKills = get_stat_value(part, 'stats', 'tripleKills')
        quadraKills = get_stat_value(part, 'stats', 'quadraKills')
        pentaKills = get_stat_value(part, 'stats', 'pentaKills')
        totalDamageDealt = get_stat_value(part, 'stats', 'totalDamageDealt')
        magicDamageDealt = get_stat_value(part, 'stats', 'magicDamageDealt')
        physicalDamageDealt = get_stat_value(part, 'stats', 'physicalDamageDealt')
        trueDamageDealt = get_stat_value(part, 'stats', 'trueDamageDealt')
        largestCriticalStrike = get_stat_value(part, 'stats', 'largestCriticalStrike')
        totalDamageDealtToChampions = get_stat_value(part, 'stats', 'totalDamageDealtToChampions')
        magicDamageDealtToChampions = get_stat_value(part, 'stats', 'magicDamageDealtToChampions')
        physicalDamageDealtToChampions = get_stat_value(part, 'stats', 'physicalDamageDealtToChampions')
        trueDamageDealtToChampions = get_stat_value(part, 'stats', 'trueDamageDealtToChampions')
        totalHeal = get_stat_value(part, 'stats', 'totalHeal')
        damageSelfMitigated = get_stat_value(part, 'stats', 'damageSelfMitigated')
        damageDealtToObjectives = get_stat_value(part, 'stats', 'damageDealtToObjectives')
        damageDealtToTurrets = get_stat_value(part, 'stats', 'damageDealtToTurrets')
        timeCCingOthers = get_stat_value(part, 'stats', 'timeCCingOthers')
        totalDamageTaken = get_stat_value(part, 'stats', 'totalDamageTaken')
        magicalDamageTaken = get_stat_value(part, 'stats', 'magicalDamageTaken')
        physicalDamageTaken = get_stat_value(part, 'stats', 'physicalDamageTaken')
        trueDamageTaken = get_stat_value(part, 'stats', 'trueDamageTaken')
        goldEarned = get_stat_value(part, 'stats', 'goldEarned')
        goldSpent = get_stat_value(part, 'stats', 'goldSpent')
        turretKills = get_stat_value(part, 'stats', 'turretKills')
        inhibitorKills = get_stat_value(part, 'stats', 'inhibitorKills')
        totalMinionsKilled = get_stat_value(part, 'stats', 'totalMinionsKilled')
        neutralMinionsKilled = get_stat_value(part, 'stats', 'neutralMinionsKilled')
        neutralMinionsKilledTeamJungle = get_stat_value(part, 'stats', 'neutralMinionsKilledTeamJungle')
        neutralMinionsKilledEnemyJungle = get_stat_value(part, 'stats', 'neutralMinionsKilledEnemyJungle')
        totalTimeCrowdControlDealt = get_stat_value(part, 'stats', 'totalTimeCrowdControlDealt')
        champLevel = get_stat_value(part, 'stats', 'champLevel')
        visionWardsBoughtInGame = get_stat_value(part, 'stats', 'visionWardsBoughtInGame')
        sightWardsBoughtInGame = get_stat_value(part, 'stats', 'sightWardsBoughtInGame')
        wardsPlaced = get_stat_value(part, 'stats', 'wardsPlaced')
        wardsKilled = get_stat_value(part, 'stats', 'wardsKilled')
        firstBloodKill = get_stat_value(part, 'stats', 'firstBloodKill')
        firstBloodAssist = get_stat_value(part, 'stats', 'firstBloodAssist')
        firstTowerKill = get_stat_value(part, 'stats', 'firstTowerKill')
        firstTowerAssist = get_stat_value(part, 'stats', 'firstTowerAssist')
        firstInhibitorKill = get_stat_value(part, 'stats', 'firstInhibitorKill')
        firstInhibitorAssist = get_stat_value(part, 'stats', 'firstInhibitorAssist')
        role = get_stat_value(part, 'timeline', 'role')
        lane = get_stat_value(part, 'timeline', 'lane')
        # key name for previous values
        highestAchievedSeasonTier_key = f'highestAchievedSeasonTier_{prefix}'
        championId_key = f'championId_{prefix}'
        kills_key = f'kills_{prefix}'
        deaths_key = f'deaths_{prefix}'
        assists_key = f'assists_{prefix}'
        largestKillingSpree_key = f'largestKillingSpree_{prefix}'
        largestMultiKill_key = f'largestMultiKill_{prefix}'
        killingSprees_key = f'killingSprees_{prefix}'
        longestTimeSpentLiving_key = f'longestTimeSpentLiving_{prefix}'
        doubleKills_key = f'doubleKills_{prefix}'
        tripleKills_key = f'tripleKills_{prefix}'
        quadraKills_key = f'quadraKills_{prefix}'
        pentaKills_key = f'pentaKills_{prefix}'
        totalDamageDealt_key = f'totalDamageDealt_{prefix}'
        magicDamageDealt_key = f'magicDamageDealt_{prefix}'
        physicalDamageDealt_key = f'physicalDamageDealt_{prefix}'
        trueDamageDealt_key = f'trueDamageDealt_{prefix}'
        largestCriticalStrike_key = f'largestCriticalStrike_{prefix}'
        totalDamageDealtToChampions_key = f'totalDamageDealtToChampions_{prefix}'
        magicDamageDealtToChampions_key = f'magicDamageDealtToChampions_{prefix}'
        physicalDamageDealtToChampions_key = f'physicalDamageDealtToChampions_{prefix}'
        trueDamageDealtToChampions_key = f'trueDamageDealtToChampions_{prefix}'
        totalHeal_key = f'totalHeal_{prefix}'
        damageSelfMitigated_key = f'damageSelfMitigated_{prefix}'
        damageDealtToObjectives_key = f'damageDealtToObjectives_{prefix}'
        damageDealtToTurrets_key = f'damageDealtToTurrets_{prefix}'
        timeCCingOthers_key = f'timeCCingOthers_{prefix}'
        totalDamageTaken_key = f'totalDamageTaken_{prefix}'
        magicalDamageTaken_key = f'magicalDamageTaken_{prefix}'
        physicalDamageTaken_key = f'physicalDamageTaken_{prefix}'
        trueDamageTaken_key = f'trueDamageTaken_{prefix}'
        goldEarned_key = f'goldEarned_{prefix}'
        goldSpent_key = f'goldSpent_{prefix}'
        turretKills_key = f'turretKills_{prefix}'
        inhibitorKills_key = f'inhibitorKills_{prefix}'
        totalMinionsKilled_key = f'totalMinionsKilled_{prefix}'
        neutralMinionsKilled_key = f'neutralMinionsKilled_{prefix}'
        neutralMinionsKilledTeamJungle_key = f'neutralMinionsKilledTeamJungle_{prefix}'
        neutralMinionsKilledEnemyJungle_key = f'neutralMinionsKilledEnemyJungle_{prefix}'
        totalTimeCrowdControlDealt_key = f'totalTimeCrowdControlDealt_{prefix}'
        champLevel_key = f'champLevel_{prefix}'
        visionWardsBoughtInGame_key = f'visionWardsBoughtInGame_{prefix}'
        sightWardsBoughtInGame_key = f'sightWardsBoughtInGame_{prefix}'
        wardsPlaced_key = f'wardsPlaced_{prefix}'
        wardsKilled_key = f'wardsKilled_{prefix}'
        firstBloodKill_key = f'firstBloodKill_{prefix}'
        firstBloodAssist_key = f'firstBloodAssist_{prefix}'
        firstTowerKill_key = f'firstTowerKill_{prefix}'
        firstTowerAssist_key = f'firstTowerAssist_{prefix}'
        firstInhibitorKill_key = f'firstInhibitorKill_{prefix}'
        firstInhibitorAssist_key = f'firstInhibitorAssist_{prefix}'
        role_key = f'role_{prefix}'
        lane_key = f'lane_{prefix}'
        # dictionary for current team
        iter_stats = {
            highestAchievedSeasonTier_key: highestAchievedSeasonTier,
            championId_key: championId,
            kills_key: kills,
            deaths_key: deaths,
            assists_key: assists,
            largestKillingSpree_key: largestKillingSpree,
            largestMultiKill_key: largestMultiKill,
            killingSprees_key: killingSprees,
            longestTimeSpentLiving_key: longestTimeSpentLiving,
            doubleKills_key: doubleKills,
            tripleKills_key: tripleKills,
            quadraKills_key: quadraKills,
            pentaKills_key: pentaKills,
            totalDamageDealt_key: totalDamageDealt,
            magicDamageDealt_key: magicDamageDealt,
            physicalDamageDealt_key: physicalDamageDealt,
            trueDamageDealt_key: trueDamageDealt,
            largestCriticalStrike_key: largestCriticalStrike,
            totalDamageDealtToChampions_key: totalDamageDealtToChampions,
            magicDamageDealtToChampions_key: magicDamageDealtToChampions,
            physicalDamageDealtToChampions_key: physicalDamageDealtToChampions,
            trueDamageDealtToChampions_key: trueDamageDealtToChampions,
            totalHeal_key: totalHeal,
            damageSelfMitigated_key: damageSelfMitigated,
            damageDealtToObjectives_key: damageDealtToObjectives,
            damageDealtToTurrets_key: damageDealtToTurrets,
            timeCCingOthers_key: timeCCingOthers,
            totalDamageTaken_key: totalDamageTaken,
            magicalDamageTaken_key: magicalDamageTaken,
            physicalDamageTaken_key: physicalDamageTaken,
            trueDamageTaken_key: trueDamageTaken,
            goldEarned_key: goldEarned,
            goldSpent_key: goldSpent,
            turretKills_key: turretKills,
            inhibitorKills_key: inhibitorKills,
            totalMinionsKilled_key: totalMinionsKilled,
            neutralMinionsKilled_key: neutralMinionsKilled,
            neutralMinionsKilledTeamJungle_key: neutralMinionsKilledTeamJungle,
            neutralMinionsKilledEnemyJungle_key: neutralMinionsKilledEnemyJungle,
            totalTimeCrowdControlDealt_key: totalTimeCrowdControlDealt,
            champLevel_key: champLevel,
            visionWardsBoughtInGame_key: visionWardsBoughtInGame,
            sightWardsBoughtInGame_key: sightWardsBoughtInGame,
            wardsPlaced_key: wardsPlaced,
            wardsKilled_key: wardsKilled,
            firstBloodKill_key: firstBloodKill,
            firstBloodAssist_key: firstBloodAssist,
            firstTowerKill_key: firstTowerKill,
            firstTowerAssist_key: firstTowerAssist,
            firstInhibitorKill_key: firstInhibitorKill,
            firstInhibitorAssist_key: firstInhibitorAssist,
            role_key: role,
            lane_key: lane
        }
        stats = {**stats, **iter_stats}
    return stats


if __name__ == '__main__':
    # for testing purposes
    my_dict = {
        'key_1': 1,
        'key_2': 2,
        'key_3': 3,
        'key_4': 4,
        'other_dict': {
            'key_5': 5,
            'key_6': 6,
            'another_dict': {
                'key_7': 7
            }
        }
    }
    my_value = get_stat_value(my_dict, 'other_dict', 'another_dict', 'key_7')
    print(my_value)
