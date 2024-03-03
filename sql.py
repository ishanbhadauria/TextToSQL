import sqlite3

connection=sqlite3.connect("student.db")


cursor=connection.cursor()

table_info = """Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25),MARKS INT);"""

cursor.execute(table_info)

cursor.execute('''Insert into STUDENT values('Ishan','Machine Learning','A',100)''')
cursor.execute('''Insert into STUDENT values('Diya','DEVOPS','B',90)''')
cursor.execute('''Insert into STUDENT values('Aditya','Data Science','A',86)''')
cursor.execute('''Insert into STUDENT values('Vibhav','MLOPS','C',73)''')
cursor.execute('''Insert into STUDENT values('Saksham','SDE','B',50)''')
cursor.execute('''Insert into STUDENT values('Parth','Data Science','A',69)''')
cursor.execute('''Insert into STUDENT values('Abhav','Machine Learning','A',92)''')
cursor.execute('''Insert into STUDENT values('Vedant','DEVOPS','A',54)''')

print("The inserted records are") 

data=cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close