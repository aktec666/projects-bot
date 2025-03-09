import sqlite3 

# открываем файл с базой данных
con = sqlite3.connect('marvel.db')

# создаём таблицу
def create_table():
    with con:
        con.execute("""
            CREATE TABLE marvel (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                superpower TEXT,
                status TEXT
    );
        """)


def drop_table():
    with con:
        con.execute("DROP TABLE marvel")


def insert_table():
    sql = 'INSERT INTO marvel (name, superpower, status) values(?, ?, ?)'

    data = [
        ('Халк', 'Суперсила', 'За добро'),
        ('Тор', 'Молот', 'За добро')
    ]

    with con:
        con.executemany(sql, data)


def update_table():
    with con:
        con.execute("UPDATE marvel SET status = 'За зло' WHERE name = 'Халк'")


def delete_table():
    with con:
        con.execute("DELETE FROM marvel WHERE name = 'Тор'")


def select_table():
    with con:
        data = con.execute("SELECT * FROM marvel")
    
    


select_table()