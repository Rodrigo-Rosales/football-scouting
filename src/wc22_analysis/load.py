from pathlib import Path

import duckdb

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_PATH = PROJECT_ROOT / "data" / "wc22.duckdb"

SQL_FILES = {
    "teams": PROJECT_ROOT / "sql" / "create_teams.sql",
    "matches": PROJECT_ROOT / "sql" / "create_matches.sql",
}


def create_tables() -> dict[str, int]:
    """Create the SQL tables in SQL_FILES

    Returns:
        A dict with the created table names as keys and their row count as values

    """
    created_tables = {}

    with duckdb.connect(DB_PATH) as con:
        for table, path in SQL_FILES.items():
            con.execute(path.read_text(encoding="utf-8"))
            value = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            created_tables[table] = value

    return created_tables


if __name__ == "__main__":    
    tables = create_tables()
    print(tables)

    with duckdb.connect(DB_PATH) as con:
        for table, path in SQL_FILES.items():
            con.sql(f"DESCRIBE {table}").show()