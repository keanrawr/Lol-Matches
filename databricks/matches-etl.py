# Databricks notebook source
import pyspark.sql.functions as F

# COMMAND ----------

def col_agg(fun, **mapping):
    return [fun(col).alias(alias) for col, alias in mapping.items()]


def normalize_cols(df, numerator_map, denominator_map):
    for key, numerator in numerator_map.items():
        denominator = denominator_map[key]
        df = df.withColumn(numerator, F.col(numerator) / F.col(denominator))
    return df


def rename_cols(df, mapping):
    for old, new in mapping.items():
        df = df.withColumnRenamed(old, new)
    return df

# COMMAND ----------

match = spark.read.json('dbfs:/mnt/lol/landing/europe/match/')
team = spark.read.json('dbfs:/mnt/lol/landing/europe/team/')
participant = spark.read.json('dbfs:/mnt/lol/landing/europe/participants/')

match = match\
    .withColumn('gameCreation', F.col('gameCreation') / 1000)\
    .withColumn('gameCreation', F.to_timestamp('gameCreation'))\
    .withColumn('gameStartTimestamp', F.col('gameStartTimestamp') / 1000)\
    .withColumn('gameStartTimestamp', F.to_timestamp('gameStartTimestamp'))

# COMMAND ----------

sum_cols = {
  'kills': 'kills',
  'assists': 'assists',
  'deaths': 'deaths',
  'doubleKills': 'double_kills',
  'tripleKills': 'triple_kills',
  'quadraKills': 'quadra_kills',
  'pentaKills': 'penta_kills',
  'unkilled': 'unkilled',
  'goldEarned': 'gold',
  'totalMinionsKilled': 'farm',
  'champExperience': 'total_xp',
  'itemsPurchased': 'total_items',
  'totalDamageDealt': 'total_dmg',
  'totalDamageDealtToChampions': 'total_dmg_champ',
  'damageDealtToTurrets': 'total_dmg_turr',
  'damageDealtToObjectives': 'total_dmg_obj',
  'totalDamageTaken': 'total_dmg_taken',
  'totalHeal': 'total_heal',
  'totalHealsOnTeammates': 'total_heal_other',
  'damageSelfMitigated' : 'total_shielded',
  'totalDamageShieldedOnTeammates': 'total_shielded_others',
}

max_cols = {
  'kills': 'maxp_kills',
  'goldEarned': 'maxp_gold_share',
  'totalMinionsKilled': 'maxp_farm',
  'champExperience': 'maxp_xp',
  'totalDamageDealt': 'maxp_total_dmg',
  'totalDamageDealtToChampions': 'maxp_total_dmg_champ',
  'damageDealtToTurrets': 'maxp_total_dmg_turr',
  'damageDealtToObjectives': 'maxp_total_dmg_obj',
  'totalDamageTaken': 'maxp_total_dmg_taken',
  'damageSelfMitigated' : 'maxp_total_shielded',
}

agg_cols = col_agg(F.sum, **sum_cols) + col_agg(F.max, **max_cols)

team_features = participant\
    .join(match, on=['gameId', 'matchId'])\
    .withColumn('unkilled', F.when(F.col('longestTimeSpentLiving') == 0, 1).otherwise(0))\
    .withColumn('longestTimeSpentLiving', F.when(
        F.col('longestTimeSpentLiving') == 0, 
        F.col('gameduration') / 1000
    ).otherwise(F.col('longestTimeSpentLiving')) )\
    .groupBy(*match.columns, 'teamId')\
    .agg(*agg_cols)\
    .transform(lambda df: normalize_cols(df, max_cols, sum_cols))

# COMMAND ----------

name_map = {
    'gameId': 'game_id',
    'matchId': 'match_id',
    'teamId': 'team_id',
    'gameCreation': 'created_at',
    'gameStartTimeStamp': 'started_at',
    'gameDuration': 'game_duration',
    'gameVersion': 'version',
    'mapId': 'map',
    'queueId': 'queue_id',
    'platformId' : 'platform_id',
}

dataset = team\
    .join(team_features, on=['gameId', 'matchId', 'teamId'])\
    .transform(lambda df: rename_cols(df, name_map))

# COMMAND ----------

dataset.repartition(1).write.mode('overwrite').parquet('dbfs:/mnt/lol/treated/databricks/v0')
