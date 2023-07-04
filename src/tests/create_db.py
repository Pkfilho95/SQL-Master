import sqlite3

conn = sqlite3.connect('./database.db')
cursor = conn.cursor()

sql = """
CREATE TABLE IF NOT EXISTS People(
Id int NOT NULL,
Name varchar(80),
Age int,
Country varchar(80),
Language varchar(80),
PRIMARY KEY(Id)
);
"""

cursor.execute(sql)
conn.commit()

data = [
    (1, 'Steve', 33, 'USA', 'Python'),
    (2, 'Tony', 22, 'Brazil', 'C'),
    (3, 'Bruce', 24, 'Mexico', 'JavaScript'),
    (4, 'Luke', 28, 'Germany', 'Java'),
    (5, 'Peter', 21, 'England', 'Python'),
    (6, 'Natasha', 18, 'Australia', 'Python'),
    (7, 'Carol', 25, 'Italy', 'Node'),
]

for row in data:
    sql = f"""INSERT INTO People VALUES{row}"""
    cursor.execute(sql)

conn.commit()