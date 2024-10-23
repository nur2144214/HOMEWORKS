import sqlite3 as sql

with sql.connect("students.db") as connection:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            хобби VARCHAR(30),
            имя VARCHAR(30),
            фамилия VARCHAR(30),
            год_рождения INTEGER,
            баллы_за_дз INT DEFAULT 0
        )
    """)
    # students_data = [
    #     ('Алексей', 'Иванов', 2005, 'велосипед', 8),
    #     ('Мария', 'Кузнецова', 2004, 'танцы', 12),
    #     ('Игорь', 'Чернышевский', 2006, 'шахматы', 9),
    #     ('Екатерина', 'Петрова', 2003, 'рисование', 15),
    #     ('Владислав', 'Николаев', 2005, 'футбол', 11),
    #     ('Анна', 'Максимова', 2004, 'пение', 7),
    #     ('Ольга', 'Мартынова', 2006, 'игра на гитаре', 13),
    #     ('Дмитрий', 'Смирнов', 2005, 'программирование', 5),
    #     ('Анастасия', 'Степанова', 2003, 'йога', 14),
    #     ('Сергей', 'Павлов', 2004, 'бег', 6)
    # ]
    # for student in students_data:
    #     cursor.execute('''
    #     INSERT INTO students (имя, фамилия, год_рождения, хобби, баллы_за_дз)
    #     VALUES (?, ?, ?, ?, ?)
    #     ''', student)
    cursor.execute("""SELECT * FROM students WHERE LENGTH(фамилия) >= 11""")
    print(cursor.fetchall())
    cursor.execute("""UPDATE students SET имя = 'genius' WHERE баллы_за_дз >= 10""")
    cursor.execute("""DELETE FROM students WHERE id % 2 = 0""")