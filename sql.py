import sqlite3

connection=sqlite3.connect('database.db')

cursor=connection.cursor()

table_info = """
Create table STUDENT(NAME varchar(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INTEGER);
"""

cursor.execute(table_info)

cursor.execute("INSERT INTO STUDENT VALUES('Rahul', 'Data Science', 'A', 99)")
cursor.execute("INSERT INTO STUDENT VALUES('Anita', 'Machine Learning', 'B', 92)")
cursor.execute("INSERT INTO STUDENT VALUES('Vikram', 'AI & Robotics', 'A', 95)")
cursor.execute("INSERT INTO STUDENT VALUES('Sneha', 'Data Science', 'C', 88)")
cursor.execute("INSERT INTO STUDENT VALUES('Amit', 'Machine Learning', 'B', 90)")
cursor.execute("INSERT INTO STUDENT VALUES('Pooja', 'AI & Robotics', 'A', 94)")
cursor.execute("INSERT INTO STUDENT VALUES('Ravi', 'Data Science', 'B', 89)")
cursor.execute("INSERT INTO STUDENT VALUES('Kavita', 'Machine Learning', 'C', 85)")
cursor.execute("INSERT INTO STUDENT VALUES('Suresh', 'AI & Robotics', 'A', 96)")
cursor.execute("INSERT INTO STUDENT VALUES('Divya', 'Data Science', 'B', 91)")


print("The inserted records are")

data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

connection.commit()
connection.close()