create_tables_queries = [
    '''CREATE TABLE IF NOT EXISTS tasks_names (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL UNIQUE
    )''',
    '''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name_id INTEGER NOT NULL,
        start DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        end DATETIME DEFAULT NULL,
        description TEXT DEFAULT NULL,
        FOREIGN KEY (task_name_id) REFERENCES tasks_names(id)
    )'''
]