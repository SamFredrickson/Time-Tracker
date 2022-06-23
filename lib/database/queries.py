create_tables_queries = [
     '''
        CREATE VIEW IF NOT EXISTS tasks_view 
          AS
          SELECT 
            tasks.id,
            tasks_names.name,
            tasks.start, 
            tasks.end, 
            tasks.description,
            tasks.date_created
          FROM tasks
          JOIN tasks_names ON tasks_names.id = tasks.task_name_id
    ''',
    '''
        CREATE TABLE IF NOT EXISTS tasks_names (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL UNIQUE
        )
    ''',
    '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name_id INTEGER NOT NULL,
            start DATETIME DEFAULT CURRENT_TIMESTAMP,
            end DATETIME DEFAULT NULL,
            description TEXT DEFAULT NULL,
            date_created DATE DEFAULT CURRENT_DATE,
            FOREIGN KEY (task_name_id) REFERENCES tasks_names(id)
    )
    ''',
    '''
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            new_day TIME NOT NULL DEFAULT '00:00:00' 
        )
    ''',
]