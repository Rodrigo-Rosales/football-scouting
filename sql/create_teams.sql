CREATE OR REPLACE TABLE teams(
    team_id BIGINT PRIMARY KEY,
    team_name VARCHAR
);

INSERT INTO teams (team_id, team_name)
SELECT home_team.home_team_id, home_team.home_team_name
FROM read_json('data/raw/matches_43_106.json'   )
UNION
SELECT away_team.away_team_id, away_team.away_team_name
FROM read_json('data/raw/matches_43_106.json')
