migrations = [
    '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            start DATETIME DEFAULT CURRENT_TIMESTAMP,
            end DATETIME DEFAULT NULL,
            description TEXT DEFAULT NULL,
            date_created DATE DEFAULT CURRENT_DATE
    )
    ''',
]