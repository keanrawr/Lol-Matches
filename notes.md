# Get EUW games data

1. Collect a summoner name
2. Get the account id for the summoners
3. Get their match history

# Using rekkles data

Summoner name: Robert Chase
Account id: 6ZIr4yOWQfvFM-bouEVKIL-tnOYE68PXcffkHa0Li7YjDg
Initial match: 4668193193 (june 2020)

### Some math

I grabbed the initial task match and chaged a number from `4668193193` to `4568193193`, and that resulted in about a month's difference. So I used the following logic:

```py
og  = 4_668_193_193
new = 4_568_193_193
dif = og - new
substract = dif * 9
print(og - substract)
>>> 3768193193
```

That last id corresponds to a match in September 2018, so we'll use that id as a parting point.

# Extracting elements from the API response

For data collection purposes we're going to be using the `/lol/match/v4/matches/{matchId}` endpoint. If we save the response for only one match as a _.json_ file it's more than 1,500 lines of file. So here are some of the attributes that we're going to be saving:

- gameId
- platformId
- gameCreation
- gameDuration
- queueId
- mapId
- seasonId
- gameVersion
- gameMode
- gameType

### Teams data

- teamId
- win
- firstBlood
- firstTower
- firstInhibitor
- firstBaron
- firstDragon
- firstRiftHerald
- towerKills
- inhibitorKills
- baronKills
- dragonKills
- riftHeraldKills

### Participants data

- teamId
- participantId
- highestAchievedSeasonTier
- championId

### Stats data (inside participant)

- kills
- deaths
- assists
- largestKillingSpree
- largestMultiKill
- killingSprees
- longestTimeSpentLiving
- doubleKills
- tripleKills
- quadraKills
- pentaKills
- totalDamageDealt
- magicDamageDealt
- physicalDamageDealt
- trueDamageDealt
- largestCriticalStrike
- totalDamageDealtToChampions
- magicDamageDealtToChampions
- physicalDamageDealtToChampions
- trueDamageDealtToChampions
- totalHeal
- damageSelfMitigated
- damageDealtToObjectives
- damageDealtToTurrets
- timeCCingOthers
- totalDamageTaken
- magicalDamageTaken
- physicalDamageTaken
- trueDamageTaken
- goldEarned
- goldSpent
- turretKills
- inhibitorKills
- totalMinionsKilled
- neutralMinionsKilled
- neutralMinionsKilledTeamJungle
- neutralMinionsKilledEnemyJungle
- totalTimeCrowdControlDealt
- champLevel
- visionWardsBoughtInGame
- sightWardsBoughtInGame
- wardsPlaced
- wardsKilled
- firstBloodKill
- firstBloodAssist
- firstTowerKill
- firstTowerAssist
- firstInhibitorKill
- firstInhibitorAssist

### Timeline data (inside participant)

- role
- lane

# Saving the values

For this data extraction we'll be saving the output as JSON, this is just for quality issues, so that when we convert them with pandas to a data frame if any of the response objects are in another oder pandas will arrange them correctly. Example output:

```json
[
  {
    "Something": "Value"
  }
]
```

# Ideas using aws

Take advantage of the cloud infrastructure, here's my idea for using aws:

1. s3: for saving output and logs, since it's way cheaper than mounting a large SSD
2. EC2: To execute the code. Since data gathering will take a loooong time, it'll be good to have a free-tier machine to execute the code. Also this'll be great to actually train the model in a big machine.
3. RDS: To have a place to save the match data outputs to, maybe postgres or maybe try redshift
3. glue: To have an ETL to grab the data from the s3 bucket to RDS
