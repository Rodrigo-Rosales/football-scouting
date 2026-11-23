# football-scouting

Find players who play alike, and see how the transfer market values them.

A scouting tool built on [StatsBomb's open data](https://github.com/statsbomb/open-data) for the 2022 FIFA World Cup (Eventually it will include more tournamets). It turns every pass, shot and tackle into per-player profiles, groups players by playing style, and joins them to their market values. The goal: pick a player, and find the most similar players, sorted by price.

## Status

Early stage, built in public. Match and team data load into DuckDB; event data is next.

| Stage | What | Status |
| --- | --- | --- |
| 1. Explore | Load matches, events and lineups; first SQL questions | In progress |
| 2. Structure | Typed package, data quality checks, tests, CI | Planned |
| 3. Model | dbt models for per-player stats; join Transfermarkt values | Planned |
| 4. Analyze | Player profiles with k-means clustering; market value findings | Planned |
| 5. Serve | Streamlit app: similar players, sorted by value | Planned |

## How it works

```
StatsBomb open data (JSON) → extract.py → data/raw/ → load.py + sql/ → DuckDB (data/football.duckdb)
```

1. **Extract:** `extract.py` downloads raw files into `data/raw/`, unchanged.
2. **Load:** `load.py` runs the SQL files in `sql/`, which rebuild each table from the raw files.
3. Every table can be rebuilt from raw at any time; nothing is edited by hand.

The tables, their grain and their known gaps are documented in [docs/data_model.md](docs/data_model.md).

## Getting started

Requires [uv](https://docs.astral.sh/uv/). Run every command from the project root.

```bash
uv sync                                    # install dependencies into .venv
uv run python -m football_scouting.extract  # download the World Cup 2022 match list
uv run python -m football_scouting.load     # build the DuckDB tables; prints row counts
```

## Development

```bash
uv run ruff check .        # lint Python
uv run ruff format         
uv run sqlfluff lint sql/  # lint SQL (DuckDB dialect)
```

Every change goes through a branch and a pull request into `main`.

## Project layout

```
src/football_scouting/   Python package: extract.py, load.py
sql/                     one SQL file per table
docs/                    data model
data/                    raw downloads and the DuckDB file (not committed)
```

## Data

Event data: [StatsBomb Open Data](https://github.com/statsbomb/open-data), used under the [StatsBomb public data user agreement](https://github.com/statsbomb/open-data/blob/master/LICENSE.pdf). Credit to StatsBomb for providing it.
