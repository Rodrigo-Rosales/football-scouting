CREATE OR REPLACE TABLE matches (
    match_id BIGINT PRIMARY KEY,
    match_date DATE,
    kick_off TIME,
    competition_id BIGINT,
    season_id BIGINT,
    stage_id BIGINT,
    stage_name VARCHAR,
    match_week INTEGER,
    home_team_id BIGINT,
    away_team_id BIGINT,
    home_score INTEGER,
    away_score INTEGER,
    stadium_id BIGINT,
    referee_id BIGINT
);

INSERT INTO matches (
    match_id,
    match_date,
    kick_off,
    competition_id,
    season_id,
    stage_id,
    stage_name,
    match_week,
    home_team_id,
    away_team_id,
    home_score,
    away_score,
    stadium_id,
    referee_id
)
SELECT
    match_id,
    match_date,
    kick_off,
    competition.competition_id,
    season.season_id,
    competition_stage.id,
    competition_stage.name,
    match_week,
    home_team.home_team_id,
    away_team.away_team_id,
    home_score,
    away_score,
    stadium.id AS stadium_id,
    referee.id AS referee_id
FROM read_json('data/raw/matches_43_106.json');
