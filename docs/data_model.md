# Data model

- Source: `data/raw/matches_43_106.json`, from StatsBomb open data (World Cup 2022: competition 43, season 106).
- Built: matches, teams. Planned: competitions, seasons, stadiums, referees.

## `matches`

**Grain:** one row per match.

| Field | Type | Notes |
| --- | --- | --- |
| match_id | BIGINT | PK |
| match_date | DATE |  |
| kick_off | TIME | Local time; StatsBomb doesn't state the timezone. |
| competition_id | BIGINT | FK → competitions.competition_id |
| season_id | BIGINT | FK → seasons.season_id |
| stage_id | BIGINT | StatsBomb stage id. No stages table; see Decisions | 
| stage_name | VARCHAR |  |
| match_week | INTEGER |  | 
| home_team_id | BIGINT | FK → teams.team_id |
| away_team_id | BIGINT | FK → teams.team_id |
| home_score | INTEGER | Includes extra time but not penalty shootouts |
| away_score | INTEGER | Includes extra time but not penalty shootouts |
| stadium_id | BIGINT | FK → stadiums.stadium_id |
| referee_id | BIGINT | FK → referees.referee_id, Allow NULL |

Built by: `sql/create_matches.sql`.

### Fields left out
- Delivery metadata (`match_status`, `match_status_360`, `last_updated`, `last_updated_360`, `metadata`): describes the file, not the match.
- Belongs in another table (managers, stadium and referee names and countries, team country): goes in its own table when a question needs it.
- No information (`team_gender`): every value is male.
- Belongs to a team within a tournament, not to a match (`home_team_group`, `away_team_group`).

Everything left out is still in data/raw/; tables can be rebuilt from it.

## `teams`

**Grain:** one row per team.

| Field | Type | Notes |
| --- | --- | --- |
| team_id | BIGINT | PK |
| team_name | VARCHAR |  |

Built by: `sql/create_teams.sql`.

## Decisions
- `stage_name` is kept next to `stage_id` instead of in a stages table: stages are a short, fixed list of labels.
- Foreign keys are documented but not declared; they'll be checked by tests, as in analytics warehouses.

## Known gaps
- Scores include extra time but not penalty shootouts. The final reads 3–3, so the winner of a drawn knockout match can't be read from matches. It's in the events data.
- The kick-off timezone isn't stated.
- "Home" and "away" are labels, not venues. Everyone except Qatar played on neutral ground, so don't analyze home advantage with this data.
- away_team_group is null even in the group stage. Use the home team's value.
- StatsBomb publishes corrections. A re-download can change values, so tables are always rebuilt from raw, never edited by hand.
